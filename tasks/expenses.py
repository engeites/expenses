from flask import Blueprint, request, render_template
import datetime
import tasks.database as db
from .utils import\
    retrieve_year_from_db, \
    retrieve_all_from_db,\
    get_today_statistics, \
    get_week_statistics, \
    get_month_statistics, \
    get_all_entries, \
    get_start_end_date_statistics

expenses = Blueprint('expenses',
                     __name__,
                     url_prefix='/exp',
                     template_folder='templates',
                     static_folder='static')


def add_expense(data):
    r = db.insert_to_db('expense', data)
    print(r)


@expenses.route('/')
def index():
    return "tasks!"


@expenses.route('/add', methods=['GET', 'POST'])
def add_task():
    # TODO: This route needs to be reconsidered -> make add_expense func return a result
    if request.method == "POST":
        values = request.get_json()
        add_expense(values)
        return f"success!"


@expenses.route('/sum/all')
def get_all_expenses_sum():
    return {
        "All spendings": retrieve_all_from_db()
    }


@expenses.route('/sum/period', methods=["POST"])
def get_period_expenses_sum():
    values = request.get_json()

    return {
        "Period spendings": get_start_end_date_statistics(**values)
    }


@expenses.route('/sum/year')
def get_last_year_expenses_sum():
    return {
        "This year spending": retrieve_year_from_db(datetime.datetime.now())
    }


@expenses.route('/sum/month')
def get_last_month_expenses_sum():
    return {
        "This month spending": get_month_statistics()
    }


@expenses.route('/sum/week')
def get_last_week_expenses_sum():
    data = get_week_statistics()
    return {
        "week": data
        # "This month spending": retrieve_month_from_db(datetime.datetime.now())
    }


@expenses.route('/sum/day')
def get_today_expenses_sum():
    return {
        "today": get_today_statistics()
    }

    pass


@expenses.route('/all')
def get_all_expenses():
    all_entries = get_all_entries()
    summ = get_all_expenses_sum()

    return render_template('show_expenses.html', entries=all_entries, sum=summ)
