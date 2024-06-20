"""API"""

import requests


class CurrencyConverter:
    """Currency converter"""
    API_URL = "https://v6.exchangerate-api.com/v6/"
    API_KEY = "39f6150997b8d9433e78f6d1"

    def __init__(self):
        self.rates = {}

    def get_rates(self, base_currency):
        """API request"""
        url = f"{self.API_URL}{self.API_KEY}/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        if data['result'] == "success":
            self.rates = data['conversion_rates']
        else:
            raise Exception("API request failed")

    def convert(self, from_currency, to_currency, amount):
        """convert"""
        self.get_rates(from_currency)

        if to_currency in self.rates:
            return amount * self.rates[to_currency]
        else:
            raise ValueError(f"No rate found for {to_currency}")


def main():
    """Main function"""
    converter = CurrencyConverter()

    from_currency = input("Enter the currency to be converted (example, USD, EUR, UAH, PLN, JPY or other ): ").upper()
    to_currency = input("Enter the currency you want to convert to (example, USD, EUR, UAH, PLN or other): ").upper()
    amount = float(input("Enter the amount to convert: "))

    try:
        converter.get_rates(from_currency)
        result = converter.convert(from_currency, to_currency, amount)
        rounded_result = round(result, 2)
        print(f"{amount} {from_currency} is equal to {rounded_result} {to_currency}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
