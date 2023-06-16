class Budget:
    def __init__(self, initial_amount, currency):
        self.balance = initial_amount
        self.currency = currency

    def update_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def get_balance_with_currency(self):
        return f"Поточний баланс: {self.balance} {self.currency}"


class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates:
            rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
            converted_amount = amount * rate
            return converted_amount
        else:
            return "Invalid currencies"


# Приклад використання

initial_amount = 1000  # Початковий бюджет
currency = "USD"  # Початкова валюта
budget = Budget(initial_amount, currency)

print(budget.get_balance_with_currency())

while True:
    action = input("Введіть дію (+/-/convert/exit): ")

    if action == "convert":
        new_currency = "UAH" if budget.currency == "USD" else "USD"

        exchange_rates = {
            "USD": 1,  # Курс долара до євро
            "UAH": 37,  # Курс гривні до євро
            # Додайте інші курси валют за потреби
        }
        converter = CurrencyConverter(exchange_rates)

        converted_amount = converter.convert(budget.get_balance(), budget.currency, new_currency)
        if isinstance(converted_amount, float):
            print(budget.get_balance_with_currency(), "=", converted_amount, new_currency)
            budget.currency = new_currency
            budget.balance = converted_amount
        else:
            print(converted_amount)

    elif action == "exit":
        break

    elif action.startswith(("+", "-")):
        amount = action[1:]
        if amount.isnumeric():
            amount = float(amount)
            if action.startswith("+"):
                budget.update_balance(amount)
            elif action.startswith("-"):
                budget.update_balance(-amount)
            print("Оновлений баланс:", budget.get_balance_with_currency())
        else:
            print("Некоректна сума")

    else:
        print("Некоректна дія. Спробуйте ще раз.")

print("Програма завершена.")
