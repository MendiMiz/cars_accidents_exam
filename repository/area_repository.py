from datetime import datetime
from typing import Dict

from bson import ObjectId

from database.connect import all_accidents, daily_statistics
from utils.data_utils import parse_date


def count_by_area(area, accidents = all_accidents):
    return accidents.count_documents({'area': area})

def count_by_area_and_day(area, date, statistics = daily_statistics):
    try:
        day_date = datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        return "Invalid date format. Please use YYYY/MM/DD."

    day_statistics = statistics.find_one({'area': area, 'date': day_date},  {'total_accidents': 1, '_id': 0})

    if day_statistics:
        return day_statistics.get('total_accidents', 0)
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


# print(get_incident_by_reason_in_area('225'))
# print(count_by_area_and_day('225', '2023-09-05'))
