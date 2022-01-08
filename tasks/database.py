import sqlite3
import os

conn = sqlite3.connect(os.path.join("tasks", "tasks.db"), check_same_thread=False)
cursor = conn.cursor()


def _create_db():
    with open(os.path.join('tasks', 'create_db.sql'), 'r', encoding='utf-8') as fout:
        sql = fout.read()

    cursor.executescript(sql)
    print('script has been executed!')
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


check_db_exists()



