import asyncio
from dataclasses import dataclass


@dataclass
class Job:
    id: int
    name: str
    attempts: int = 0


async def process(job: Job) -> None:
    await asyncio.sleep(0)


async def worker(queue: asyncio.Queue[Job], completed: list[int]) -> None:
    while True:
        job = await queue.get()
        try:
            job.attempts += 1
            await process(job)
            completed.append(job.id)
        finally:
            queue.task_done()


async def run_demo() -> list[int]:
    queue: asyncio.Queue[Job] = asyncio.Queue()
    completed: list[int] = []
    task = asyncio.create_task(worker(queue, completed))
    await queue.put(Job(1, "report"))
    await queue.join()
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass
    return completed


if __name__ == "__main__":
    print(asyncio.run(run_demo()))
