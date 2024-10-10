from flask import Blueprint, request, jsonify
from repository.area_repository import count_by_area, count_by_area_and_day
from utils.rand_utils import parse_json

area_blueprint = Blueprint("area", __name__)



@area_blueprint.route('/<area_id>', methods=['GET'])
def count_accidents_by_area(area_id):
    accidents_count = count_by_area(area_id)
    return jsonify({"accidents_count": accidents_count}), 200

@area_blueprint.route('/<area_id>/<date>', methods=['GET'])
def count_accidents_by_area_and_date(area_id, date):
    accidents_count = count_by_area_and_day(area_id, date)
    return jsonify({"accidents_count": accidents_count}), 200

