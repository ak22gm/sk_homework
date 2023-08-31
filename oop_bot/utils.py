import requests
import json
from config import keys

class ConvertionException (Exception):
    pass
class Cnvrtor:
    @staticmethod
    def get_price(quote: str, base: str, amount:str):
        if quote == base:
            raise ConvertionException(f'Невыбрана валютная пара {base}!')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Невозможно конвертировать {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Невозможно конвертировать {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неправльное значение {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return round(total_base*amount, 2)
