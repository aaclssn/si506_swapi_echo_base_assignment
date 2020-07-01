import requests
import json

ENDPOINT = 'http://swapi.py4e.com/api'
resource = '/starships/'
params = {'search':'Luke Skywalker'}

url = ENDPOINT + resource

SHIP = (
    'name', 'model', 'manufacturer', 'length', 'width', 'max_atmosphering_speed', 'crew', 'passengers',
    'cargo_capacity', 'consumables', 'hyperdrive_rating', 'MGLT',
    'starship_class', 'armament', 'url'
)

PERSON_KEYS = (
    'url', 'name', 'alias', 'rank', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
    'gender', 'homeworld', 'species'
)

PLANET_KEYS = (
    'url', 'name', 'natural_satellites', 'rotation_period', 'orbital_period', 'diameter',
    'climate', 'gravity', 'terrain', 'surface_water', 'population'
)

PLANET_HOTH_KEYS = (
    'url', 'name', 'system_position', 'natural_satellites', 'rotation_period', 'orbital_period', 'diameter',
    'climate', 'gravity', 'terrain', 'surface_water', 'population', 'indigenous_life_forms'
)

SPECIES_KEYS = ('url', 'name', 'classification', 'designation', 'average_height', 'skin_colors',
 'hair_colors', 'eye_colors', 'average_lifespan', 'language')

VEHICLE_KEYS = (
    'url', 'vehicle_class', 'name', 'manufacturer', 'length',
    'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity', 'consumables', 'armament'
)


filename = '../output/final.json'

def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data

def get_swapi_resource(url, params=None):
    response_lst = []
    response = requests.get(url, params=None).json()
    for item in response['results']:
        response_lst.append(item)
    while response['next'] is not None:
        response = requests.get(response['next']).json() # is called 7 times and returns a response with 10 dictionaries each
        for item in response['results']:
            response_lst.append(item)

    print(json.dumps(response_lst, indent=2))
    return response_lst


def combine_data(default_data, override_data):
    combined_data = default_data.copy()  # shallow
    # print(json.dumps(default_data[0], indent=2), '\n\n')
    # print(json.dumps(override_data, indent=2))
    # print(len(override_data))

### HERE
def filter_data(data, filter_keys):
    record = {}
    for key in filter_keys:
        if key in data.keys():
            record[key] = data[key]

    return record


def is_unknown(value):
    pass

def convert_string_to_float(value):
    pass

def convert_string_to_int(value):
   pass


def convert_string_to_list(value, delimiter=','):
    pass

def clean_data(entity):
    pass

def extract(data, lst):
    lst_data = []
    for entity in data:
        lst_data.append(entity)
    return lst_data

def assign_crew(entity, crew):
    pass

def write_json(filename, data):
    with open(filename, 'w', encoding='utf8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    ENDPOINT = 'http://swapi.py4e.com/api'
    resource = '/planets/'
    url = ENDPOINT + resource

    filepath = '../input/default/swapi_planets-v1p0.json'
    filename = '../output/final.json'

    basic_info = read_json(filepath)
    planets_results = get_swapi_resource(url)

    planet = combine_data(basic_info, planets_results)
    # planet = filter_data(planet, PLANET_KEYS)
    #
    # basic_info = planet
    #
    # write_json(filename, basic_info)

if __name__ == '__main__':
    main()
