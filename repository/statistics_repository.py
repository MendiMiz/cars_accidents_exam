from typing import Dict

from bson import ObjectId

from database.connect import all_accidents


def count_by_area(area ,accidents = all_accidents):
    return accidents.count_documents({'area': area})

def count_by_area_and_day(area, day, )

# def insert_car( new_car: Dict, cars_collection = cars):
#     return cars_collection.insert_one(new_car).inserted_id
#
# def update_one_car(car_id, update_data: Dict, cars_collection = cars):
#     res = cars_collection.update_one(
#         {'_id': ObjectId(car_id)},
#         {'$set': update_data}
#     )
#     return res
#
# def delete_car_by_id(car_id, cars_collection = cars):
#     res = cars_collection.delete_one({'_id': ObjectId(car_id)})
#     return res

print(count_by_area('225'))
