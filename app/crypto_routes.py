from app import app
from time import time
from flask import jsonify, render_template

from app.API_classes import PriceObtainer, AllCurrencies


@app.route("/crypto/<string:token>")
def return_token_price(token):
    """
    This endpoint returns token last price according to the currency.com
    :param token: string with short name of crypto: btc, eth, cake, etc.
    :return: price in float
    """
    getter = PriceObtainer(token)
    price = getter.run()
    return price


@app.route("/currs")
def get_currs():
    """
    This endpoint returns a response of currency.com (all available token pairs: btc/usdt,
    eth/usd, etc. in one large json file that is loaded in html
    :return: html template with all info
    """
    currencies = AllCurrencies()
    text = currencies.run()
    return render_template('currs.html', info=text)