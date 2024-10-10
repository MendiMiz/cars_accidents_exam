from datetime import datetime, timedelta

from database.connect import all_accidents, daily_statistics, weekly_statistics, monthly_statistics
from utils.data_utils import get_week_start


def count_by_area(area, accidents = all_accidents):
    return accidents.count_documents({'area': area})

def count_by_area_and_day(area, date, statistics = daily_statistics):
    try:
        day_date = datetime.strptime(date, '%Y-%m-%d')
        print(day_date)
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD"

    day_statistics = statistics.find_one({'area': area, 'date': day_date},  {'total_accidents': 1, '_id': 0})

    if day_statistics:
        return day_statistics.get('total_accidents', 0)
    else:
        return "No data found for the specified area and date."

def count_by_area_and_week(area, date, statistics = weekly_statistics):
    try:
        day_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD"
    week_start = day_date - timedelta(days=day_date.weekday())

    week_statistics = statistics.find_one({'area': area, 'week_start': week_start},  {'total_accidents': 1, '_id': 0})
    if week_statistics:
        return week_statistics
    else:
        return "No data found for the specified area and date."

def count_by_area_year_month(area, year, month, statistics = monthly_statistics):

    month_statistics = statistics.find_one({'area': area, 'year': year, 'month': month},  {'total_accidents': 1, '_id': 0})

    if month_statistics:
        return month_statistics
    else:
        return "No data found for the specified area and date."



def get_incident_by_reason_in_area(area, accidents = all_accidents):
    pipeline = [
        {
            '$match': {'area': area}
        },
        {
            '$group': {
                '_id': '$contributing_factor',
                'total_incidents': {'$sum': 1},
                'accidents_list': {'$push': '$$ROOT'}
            }
        },
        {
            '$project': {
                'contributing_factor': '$_id',
                'total_incidents': 1,
                'accidents_list': 1,
                '_id': 0
            }
        }
    ]

    aggregation = accidents.aggregate(pipeline)

    result = {
        'area': area,
        'contributing_factor': list(aggregation)
    }

    return result


def get_injuries_and_fatal_by_area(area, accidents = all_accidents):
    pipeline = [
        {
            '$match': {'area': area}
        },
        {
            '$group': {
                '_id': '$area',
                'total_injuries': {'$sum': '$injuries.total'},
                'fatal_injuries': {'$sum': '$injuries.fatal'},
                'non_fatal_injuries': {'$sum': '$injuries.non_fatal'},
                'accidents_list': {'$push': '$$ROOT'}
            }
        },
        {
            '$project': {
                'area': '$_id',
                'total_injuries': 1,
                'fatal_injuries': 1,
                'non_fatal_injuries': 1,
                'accidents_list': 1,
                '_id': 0
            }
        }
    ]

    aggregation = accidents.aggregate(pipeline)
    res = list(aggregation)[0]


    return res

print(get_incident_by_reason_in_area('225'))
# print(get_injuries_and_fatal_by_area('225'))
print(count_by_area_and_day('225', '2023-09-05'))
print(count_by_area_and_week('411', '2023-09-19'))
print(count_by_area_year_month('1650', 2023, '8'))


