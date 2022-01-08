import requests


class PriceObtainer:

    def __init__(self, token):
        self.link = "https://api-adapter.backend.currency.com"
        self.request = "/api/v1/ticker/24hr"
        self.payload = {"symbol": f"{token}/USD"}

    def get_response(self):
        response = requests.get(f"{self.link}{self.request}", params=self.payload)
        return response

    @staticmethod
    def parse_response(response):
        dictionary = response.json()
        return dictionary

    @staticmethod
    def cut_the_shit(shit):
        """This func extracts just 'last price' field fom response body"""
        return shit['lastPrice']

    def run(self):

        response = self.get_response()
        print(response.status_code)
        if response.status_code == 400:
            return {'code': "1001", "msg": "This token is unavailable"}
        return {"last_price": self.cut_the_shit(self.parse_response(response))}


class AllCurrencies:
    link = "https://api-adapter.backend.currency.com/api/v1/exchangeInfo"

    def _get_info(self):
        return requests.get(self.link)

    @staticmethod
    def jsonify_it(info):
        return info.json()

    def run(self):
        info = self._get_info()
        return self.jsonify_it(info)
