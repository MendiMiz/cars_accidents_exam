from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
car_accidents = client['car_accidents']

all_accidents = car_accidents['all_accidents']
daily_statistics = car_accidents['daily_statistics']
weekly_statistics = car_accidents['weekly_statistics']
monthly_statistics = car_accidents['monthly_statistics']