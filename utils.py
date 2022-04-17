import json


def get_test_data(filename):
    with open(f'./data/{filename}', 'r') as f:
        data = json.load(f)

    data = data['data']
    return [(d['input'], d['output']) for d in data]