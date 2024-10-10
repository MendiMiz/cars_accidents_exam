from flask import Blueprint, request, jsonify
from repository.csv_repository import init_car_accidents

db_blueprint = Blueprint("db", __name__)



@db_blueprint.route('/initialize_db', methods=['POST'])
def count_accidents_by_area():
    status = init_car_accidents()
    return jsonify({"initialize status": status}), 200
