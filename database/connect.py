from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
car_accidents = client['car_accidents']

daily_based = car_accidents['daily_based']
weekly_based = car_accidents['weekly_based']
monthly_based = car_accidents['monthly_based']