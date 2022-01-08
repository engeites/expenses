from extentions import db
from API_classes import PriceObtainer
from config import ASSETS


def sched_task():
    for i in ASSETS:
        getter = PriceObtainer(i)
        price = getter.run()
        db.add_entry(price['last_price'], i)
        print(f"Added a new entry into database: {i}: {price['last_price']}")
