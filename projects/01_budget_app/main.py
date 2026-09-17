from budget import calculate_balance, parse_amount


def read_amount(prompt: str):
    while True:
        try:
            return parse_amount(input(prompt))
        except ValueError as error:
            print(error)


def main() -> None:
    income = read_amount("Доход за месяц: ")
    expenses = []
    while True:
        raw = input("Расход или 'стоп': ").strip()
        if raw.lower() == "стоп":
            break
        try:
            expenses.append(parse_amount(raw))
        except ValueError as error:
            print(error)

    total, balance, percent = calculate_balance(income, expenses)
    print(f"Расходы: {total} руб.")
    print(f"Остаток: {balance} руб.")
    print(f"Доля расходов: {percent}%")


if __name__ == "__main__":
    main()
