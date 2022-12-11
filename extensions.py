import requests

import json

class ConvertionException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        quote, base, amount = values

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты{base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту{base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
