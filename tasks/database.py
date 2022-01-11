import sqlite3
import os

conn = sqlite3.connect(os.path.join("tasks", "tasks.db"), check_same_thread=False)
cursor = conn.cursor()


def _create_db():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(THIS_FOLDER, 'create_db.sql'), 'r', encoding='utf-8') as fout:
        sql = fout.read()

    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='expense'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _create_db()


def insert_to_db(table: str, column_values:dict):
    columns = ", ".join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ', '.join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table}"
        f"({columns})"
        f"VALUES ({placeholders})", values)
    conn.commit()


def retrieve_from_start_date(start_date):
    cursor.execute(
        f"SELECT sum(amount) FROM expense "
        f"WHERE date(created_time) >= '{start_date}' "
    )
    a = cursor.fetchone()
    return a[0]


def retrieve_from_start_to_end_date(start_date, end_date):
    cursor.execute(
        f"SELECT sum(amount) FROM expense "
        f"WHERE date(created_time) >= '{start_date}' "
        f"AND date(created_time) <= '{end_date}';"
    )
    a = cursor.fetchone()
    return a


def retrieve_category(category):
    cursor.execute(
        f"SELECT sum(amount) FROM expense "
        f"WHERE category_codename = '{category}';"
    )
    a = cursor.fetchone()
    return a[0]


def retrieve_category_by_date(category, start_date, end_date):
    cursor.execute(
        f"SELECT sum(amount) FROM expense "
        f"WHERE category_codename = '{category}' "
        f"AND date(created_time) >= '{start_date}' "
        f"AND date(created_time) <= '{end_date}';"
    )
    a = cursor.fetchone()
    return a[0]


def retrieve_week_from_db(date):
    # cannot delete this func now due to flask error. Try again later
    pass


def retrieve_year_from_db(start_date):
    # cannot delete this func now due to flask error. Try again later
    pass


def retrieve_today_from_db():
    cursor.execute(
        f"SELECT sum(amount) FROM expense "
        f"WHERE date(created_time) = date('now', 'localtime') "
    )
    a = cursor.fetchone()
    return a[0]


def retrieve_all_from_db():
    cursor.execute(
        f"SELECT sum(amount) FROM expense "
    )
    a = cursor.fetchone()
    return a[0]


def retrieve_all_entries_from_db():
    cursor.execute(
        f"SELECT * FROM expense "
        f"order by created_time desc"
    )
    a = cursor.fetchall()
    return a


def retrieve_categories():
    cursor.execute(
        f"SELECT * FROM category"
    )
    return cursor.fetchall()


check_db_exists()



