import sqlite3
from time import time


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("price_change.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        command1 = """CREATE TABLE IF NOT EXISTS
        btc_history(price REAL, time TEXT);"""
        command2 = """CREATE TABLE IF NOT EXISTS
        eth_history(price REAL, time TEXT);"""
        self.cursor.execute(command1)
        self.cursor.execute(command2)

    def add_entry(self, price, token):
        milliseconds = lambda: int(time() * 1000)
        self.cursor.execute(f"""INSERT INTO {token}_history VALUES (?, ?);""", (price, milliseconds()))
        self.connection.commit()

    def close_db(self):
        self.connection.close()


def open_db():
    connection = sqlite3.connect("price_change.db", check_same_thread=False)
    cursor = connection.cursor()

    command = """SELECT name FROM sqlite_master WHERE type='table';"""
    results = cursor.execute(command).fetchall()
    print(results)
    command2 = """SELECT * FROM btc_history;"""
    results = cursor.execute(command2).fetchall()
    print(results)
    connection.close()


if __name__ == '__main__':
    open_db()
