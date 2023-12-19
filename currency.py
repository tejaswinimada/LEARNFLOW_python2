class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("Invalid currency.")
            return None

        if from_currency == to_currency:
            return amount  # No conversion needed

        if from_currency != "USD":
            amount_in_usd = amount / self.exchange_rates[from_currency]
        else:
            amount_in_usd = amount

        if to_currency == "USD":
            converted_amount = amount_in_usd
        else:
            converted_amount = amount_in_usd * self.exchange_rates[to_currency]

        return round(converted_amount, 2)

# Example usage:
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "INR": 70,
}

converter = CurrencyConverter(exchange_rates)

while True:
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

    converted_amount = converter.convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print("{} {} is equal to {} {}".format(amount, from_currency, converted_amount, to_currency))

    another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
    if another_conversion != "yes":
        break
