import csv
from database.connect import all_accidents, daily_statistics, weekly_statistics, monthly_statistics
from utils.data_utils import parse_date, extract_year, get_week_start, parse_date_only
from utils.rand_utils import num_or_zero_if_empty


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_car_accidents():
   daily_statistics.drop()
   weekly_statistics.drop()
   monthly_statistics.drop()
   all_accidents.drop()

   try:
       for row in read_csv('../data/data.csv'):
           accident = {
               'date': parse_date(row['CRASH_DATE']),
               'area': row['BEAT_OF_OCCURRENCE'],
               'injuries': {
                   'total': num_or_zero_if_empty(row['INJURIES_TOTAL']),
                   'fatal':num_or_zero_if_empty(row['INJURIES_FATAL']),
                   'non_fatal': num_or_zero_if_empty(row['INJURIES_TOTAL']) - num_or_zero_if_empty(row['INJURIES_FATAL'])
               },
               'contributing_factor': row['PRIM_CONTRIBUTORY_CAUSE']
           }

           all_accidents.insert_one(accident)


           daily_statistics.update_one(
               {'date': parse_date_only(row['CRASH_DATE']), 'area': row['BEAT_OF_OCCURRENCE']},
               {'$inc': {
                   'total_accidents': 1,
                   'injuries.total': num_or_zero_if_empty(row['INJURIES_TOTAL']),
                   'injuries.fatal': num_or_zero_if_empty(row['INJURIES_FATAL']),
                   'injuries.non_fatal': num_or_zero_if_empty(row['INJURIES_TOTAL']) - num_or_zero_if_empty(row['INJURIES_FATAL'])
               }},
               upsert=True
           )

           weekly_statistics.update_one(
               {'week_start':  get_week_start(row['CRASH_DATE']), 'area': row['BEAT_OF_OCCURRENCE']},
               {'$inc': {
                   'total_accidents': 1,
                   'injuries.total': num_or_zero_if_empty(row['INJURIES_TOTAL']),
                   'injuries.fatal': num_or_zero_if_empty(row['INJURIES_FATAL']),
                   'injuries.non_fatal': num_or_zero_if_empty(row['INJURIES_TOTAL']) - num_or_zero_if_empty(row['INJURIES_FATAL'])
               }},
               upsert=True
           )

           monthly_statistics.update_one(
               {'month': row['CRASH_MONTH'], 'year': extract_year(row['CRASH_DATE']), 'area': row['BEAT_OF_OCCURRENCE']},
               {'$inc': {
                   'total_accidents': 1,
                   'injuries.total': num_or_zero_if_empty(row['INJURIES_TOTAL']),
                   'injuries.fatal': num_or_zero_if_empty(row['INJURIES_FATAL']),
                   'injuries.non_fatal': num_or_zero_if_empty(row['INJURIES_TOTAL']) - num_or_zero_if_empty(row['INJURIES_FATAL'])
               }},
               upsert=True
           )
       return "db initialized successfully"

   except ValueError:
       return  "failed to initialize db"


init_car_accidents()