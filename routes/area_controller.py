from flask import Blueprint, request, jsonify
from repository.statistics_repository import count_by_area
from utils.rand_utils import parse_json

area_blueprint = Blueprint("area", __name__)



@area_blueprint.route('/<area_id>', methods=['GET'])
def count_accidents_by_area(area_id):
    accidents_count = count_by_area(area_id)
    return jsonify({"accidents_count": accidents_count}), 200