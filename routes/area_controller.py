from flask import Blueprint, request, jsonify
from repository.area_repository import count_by_area, count_by_area_and_day, get_incident_by_reason_in_area, \
    get_injuries_and_fatal_by_area, count_by_area_year_month, count_by_area_and_week
from utils.rand_utils import parse_json

area_blueprint = Blueprint("area", __name__)



@area_blueprint.route('/<area_id>', methods=['GET'])
def count_accidents_by_area(area_id):
    accidents_count = count_by_area(area_id)
    return jsonify({"accidents_count": accidents_count}), 200

@area_blueprint.route('/area_day/<area_id>/<day_date>', methods=['GET'])
def count_accidents_by_area_and_day(area_id, day_date):
    accidents_count = count_by_area_and_day(area_id, day_date)
    return jsonify({"accidents_count": accidents_count}), 200

@area_blueprint.route('/order_by_reason/<area_id>/', methods=['GET'])
def incident_by_reason_in_area(area_id):
    res = get_incident_by_reason_in_area(area_id)
    return parse_json(res), 200

@area_blueprint.route('/injuries/<area_id>/', methods=['GET'])
def injuries_and_fatal_by_area(area_id):
    res = get_injuries_and_fatal_by_area(area_id)
    return parse_json(res), 200

@area_blueprint.route('/area_year_month/<area_id>/<year>/<month>', methods=['GET'])
def get_count_by_area_year_month(area_id, year, month):
    res = count_by_area_year_month(area_id, int(year), month)
    return parse_json(res), 200

@area_blueprint.route('/area_week/<area_id>/<date>', methods=['GET'])
def get_count_by_area_and_week(area_id, date):
    res = count_by_area_and_week(area_id, date)
    return parse_json(res), 200