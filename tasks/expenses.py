from flask import Blueprint, request
import tasks.database as db

expences = Blueprint('expences', __name__, url_prefix='/exp')


def add_expense(data):
    r = db.insert_to_db('expense', data)
    print(r)


@expences.route('/')
def index():
    return "tasks!"


@expences.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == "POST":
        values = request.get_json()
        add_expense(values)
        return f"success!"


@expences.route('/month')
def get_last_month_expenses():
    # Обратиться к управляющей функции
    # Получить текущее время, отсчитать до начала месяца
    # Сделать запрос в базу данных за записями
    # Вернуть инфо в json

    pass