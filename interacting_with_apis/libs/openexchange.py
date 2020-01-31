import requests
import functools

class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/latest.json"

    def __init__(self, app_id):
        self.app_id = app_id

    @functools.lru_cache(maxsize=2)
    def convert(self, amount, from_currency, to_currency,):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return amount * to_rate
        else:
            from_in_usd = amount /rates[from_currency]
            return from_in_usd * to_rate

    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}?app_id={self.app_id}").json()

