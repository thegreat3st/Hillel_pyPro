import asyncio
from pprint import pprint
import requests
from time import perf_counter

class ExchangeRates():
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
            
    def __init__(self, currency: list[str]) -> None:
        self._currency = currency
        if ExchangeRates._initialized:
            return
        ExchangeRates._initialized = True
        
    async def _fetch_from_api(self) -> None:
        currency1: str
        n = 0
        while n<=5:
            for currency1 in self._currency[:]:
                url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency={currency1}&apikey=PASTE_YOUR_API_KEY"
                response = await asyncio.to_thread(requests.get, (url))
                pprint(response.json()) 
            break
        
async def main():
    
    er = ExchangeRates(["UAH", "EUR", "GBP", "PLN", "KZT"])
    tasks = [er._fetch_from_api()]
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()

    print(f"⏲️ Total time: {end-start}")