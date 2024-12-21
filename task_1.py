# TODO решите задачу

import json
def task(file) -> float:
    with open(file, 'r') as file:
        data = json.load(file)
        summ = sum(entry['score'] * entry['weight'] for entry in data)
    return round(summ, 3)
file_path = "input.json"
print(task(file_path))
