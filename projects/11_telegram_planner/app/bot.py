from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from . import repository
from .settings import BOT_TOKEN, DB_PATH


router = Router()


class TaskForm(StatesGroup):
    title = State()


def done_keyboard(task_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Готово", callback_data=f"done:{task_id}"),
    ]])


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer("Привет! Используй /add и /tasks.")


@router.message(Command("add"))
async def add_start(message: Message, state: FSMContext) -> None:
    await state.set_state(TaskForm.title)
    await message.answer("Напиши задачу одним сообщением")


@router.message(TaskForm.title)
async def add_finish(message: Message, state: FSMContext) -> None:
    title = (message.text or "").strip()
    if not title:
        await message.answer("Задача не может быть пустой")
        return
    with repository.connect(DB_PATH) as connection:
        repository.add_task(connection, message.from_user.id, title)
    await state.clear()
    await message.answer("Задача сохранена")


@router.message(Command("tasks"))
async def list_handler(message: Message) -> None:
    with repository.connect(DB_PATH) as connection:
        tasks = repository.list_open(connection, message.from_user.id)
    if not tasks:
        await message.answer("Открытых задач нет")
        return
    for task in tasks:
        await message.answer(task["title"], reply_markup=done_keyboard(task["id"]))


@router.callback_query(lambda callback: callback.data and callback.data.startswith("done:"))
async def done_handler(callback: CallbackQuery) -> None:
    task_id = int(callback.data.split(":", 1)[1])
    with repository.connect(DB_PATH) as connection:
        changed = repository.complete_task(connection, callback.from_user.id, task_id)
    await callback.answer("Готово" if changed else "Задача не найдена")
    if changed and callback.message:
        await callback.message.edit_text("Задача выполнена")


async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("Переменная BOT_TOKEN не задана")
    repository.connect(DB_PATH).close()
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)
