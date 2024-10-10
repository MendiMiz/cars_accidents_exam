from datetime import datetime, timedelta


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)

def extract_year(date_str: str):
    return parse_date(date_str).year

def get_week_start(date_str: str):
    only_date = date_str.split(" ")[0]
    date = datetime.strptime(only_date, '%m/%d/%Y')
    start = date - timedelta(days=date.weekday())
    return start


def get_week_range(date_str):
    only_date = date_str.split(" ")[0]
    date_obj = datetime.strptime(only_date, '%m/%d/%Y')
    start_of_week = date_obj - timedelta(days=date_obj.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

print(get_week_start('09/22/2023 06:50:00 PM'))