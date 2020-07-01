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

    return response_lst


def combine_data(default_data, override_data):
    combined_data = default_data.copy()  # shallow
    for old_planet_dict in combined_data:
        for new_planet_dict in override_data:
            if (old_planet_dict['name'] == new_planet_dict['name']):
                for key in list(new_planet_dict.keys()):
                    old_planet_dict[key] = new_planet_dict[key]
    return combined_data

### HERE
def filter_data(data, filter_keys):
    filtered_planet_data = []
    for planet_dict in data:
        record = {}
        for key in filter_keys:
            if key in planet_dict.keys():
                record[key] = planet_dict[key]
        filtered_planet_data.append(record)

    return filtered_planet_data


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
    filter_planet = filter_data(planet, PLANET_KEYS)
    #
    # basic_info = filter_planet
    #
    # write_json(filename, basic_info)

if __name__ == '__main__':
    main()
