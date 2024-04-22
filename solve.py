import json


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def check_resource(json_data):
    statements = json_data.get('PolicyDocument', {}).get('Statement', [])
    for statement in statements:
        if statement.get('Resource') == '*':
            return False
    return True

file_path = 'file.json'
json_data = load_json_data(file_path)
is_valid = check_resource(json_data)
print("Is JSON valid:", is_valid)