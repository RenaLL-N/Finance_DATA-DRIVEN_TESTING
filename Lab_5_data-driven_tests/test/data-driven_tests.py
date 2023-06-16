import csv
import unittest
from finance import Budget, CurrencyConverter

class BudgetTestCase(unittest.TestCase):
    def setUp(self):
        initial_amount = 1000
        currency = "USD"
        self.budget = Budget(initial_amount, currency)

    def load_test_data(self, filename):
        test_data = []
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                test_data.append(row)
        return test_data

    def test_data_driven_convert_currency(self):
        test_data = self.load_test_data('test_data.csv')
        for data in test_data:
            amount = float(data['amount'])
            from_currency = data['from_currency']
            to_currency = data['to_currency']
            expected_amount = float(data['expected_amount'])
            expected_currency = data['expected_currency']

            exchange_rates = {
                "USD": 1,
                "UAH": 27,
            }
            converter = CurrencyConverter(exchange_rates)

            converted_amount = converter.convert(amount, from_currency, to_currency)
            converted_amount = round(converted_amount, 2)
            expected_amount = round(expected_amount, 2)

            self.assertEqual(converted_amount, expected_amount,
                             f"Converted amount: {converted_amount}, Expected amount: {expected_amount}")

            self.budget.currency = to_currency
            self.budget.balance = converted_amount

            expected_balance_with_currency = f"Поточний баланс: {expected_amount} {expected_currency}"
            self.assertEqual(self.budget.get_balance_with_currency(), expected_balance_with_currency)

if __name__ == '__main__':
    unittest.main()