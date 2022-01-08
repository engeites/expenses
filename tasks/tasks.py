from flask import Blueprint, request
import tasks.database as db

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


def add_expense(data):
    r = db.insert_to_db('expense', data)
    print(r)


@tasks.route('/')
def index():
    return "tasks!"


@tasks.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == "POST":
        values = request.get_json()
        add_expense(values)

        return f"success!"
