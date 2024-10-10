import json
from bson import json_util

def num_or_zero_if_empty(num_str):
    if num_str == " " or num_str == "":
        return 0
    else:
        return int(num_str)

def parse_json(data):
    return json.loads(json_util.dumps(data))