
import datetime
from datetime import timedelta
import datetime

from tasks.database import \
    retrieve_from_start_date, \
    retrieve_all_from_db, \
    retrieve_year_from_db, \
    retrieve_today_from_db, \
    retrieve_week_from_db, \
    retrieve_all_entries_from_db, \
    retrieve_from_start_to_end_date, retrieve_category, retrieve_category_by_date, retrieve_categories


def get_now_datetime():
    return datetime.datetime.now()


def get_now_formatted() -> str:
    return get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")


def get_month_statistics():
    now = get_now_datetime()
    first_day_of_month = f'{now.year:04d}-{now.month:02d}-01'
    print(f"from get_month statistics {first_day_of_month}")
    return retrieve_from_start_date(first_day_of_month)


def get_start_end_date_statistics(start_date, end_date):
    return retrieve_from_start_to_end_date(start_date, end_date)


def get_year_statistics():
    date = datetime.datetime.now()
    first_day_of_year = f'{date.year:04d}-01-01'
    return retrieve_from_start_date(first_day_of_year)


def get_today_statistics():
    return retrieve_today_from_db()


def get_week_statistics():
    now = datetime.datetime.now()
    start_of_week = now - timedelta(days=now.weekday())
    start_of_week = start_of_week.date().strftime('%Y-%m-%d')
    return retrieve_from_start_date(start_of_week)


def get_all_statistics():
    data = retrieve_all_from_db()
    return data


def get_category_statistics(category):
    data = retrieve_category(category)
    return {category: data}


def get_category_statistics_by_date(values):
    data = retrieve_category_by_date(**values)
    return data


def get_all_entries():
    data = retrieve_all_entries_from_db()
    return data


def get_all_categories():
    return retrieve_categories()


if __name__ == '__main__':
    print(get_now_formatted())
    print(get_year_statistics())