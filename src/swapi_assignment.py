import json, requests


ENDPOINT= 'http://swapi.py4e.com/api'
search = 'people/'
r = requests.get(ENDPOINT,params={'search':search})
#print(f"Status code: {r.status_code}")
#response_dict=r.json()

#print(response_dict.keys())

print(r)

filename =" 'final.json'


def assign_crew(entity, crew):
    pass


def clean_data(entity):
    pass


def combine_data(default_data, override_data):
    pass


def convert_string_to_float(value):
    pass


def convert_string_to_int(value):
   pass


def convert_string_to_list(value, delimiter=','):
    pass


def filter_data(data, filter_keys):
    pass


def get_swapi_resource(url, params=None):
    pass


def is_unknown(value):
    pass


def read_json(filepath):
    pass


def write_json(filepath, data):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
