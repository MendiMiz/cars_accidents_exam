from repository.area_repository import count_by_area, count_by_area_and_day, get_incident_by_reason_in_area, \
    get_injuries_and_fatal_by_area, count_by_area_and_week, count_by_area_year_month

area = '225'

def test_count_by_area():
    res = count_by_area(area)
    assert res > 0

def test_count_by_area_and_day():
    date = '2023-09-05'
    res = count_by_area_and_day(area, date)
    assert res == 1

def test_get_incident_by_reason_in_area():
    res = get_incident_by_reason_in_area(area)
    assert res['area'] == '225'

def test_get_injuries_and_fatal_by_area():
    res = get_injuries_and_fatal_by_area(area)
    assert  res['total_injuries'] == 115

def test_count_by_area_and_week():
    date = '2023-09-06'
    res = count_by_area_and_week('411', '2023-09-19')
    assert res['total_accidents'] == 2

def test_count_by_area_year_month():
    res = count_by_area_year_month('1650', 2023, '8')
    assert res['total_accidents'] == 5