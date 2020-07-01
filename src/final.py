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


filename = 'final.json'

def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data

def get_swapi_resource(url, params=None):
        response_lst = []
        response = requests.get(url, params=None).json()
        response_lst.append(response)
        while response['next'] is not None:
            response = requests.get(response['next']).json()
            response_lst.append(response['results'])
        return response_lst


def combine_data(default_data, override_data):
    combined_data = default_data.copy()  # shallow
    for i in override_data:
        print(i.keys())
    print(default_data)
     # combined_data = copy.copy(default_data) # shallow
     # combined_data = copy.deepcopy(default_data) # deep
    # combined_data.update(override_data)  # in place

        # Dictionary unpacking
        # combined_data = {**default_data, **override_data}

    # return combined_data
    # combined_data = default_data.copy()  # shallow
    #
    # # combined_data =
    # # combined_data = {**default_data, **override_data}
    # # combined_data = copy.copy(default_data) # shallow
    # # combined_data = copy.deepcopy(default_data) # deep
    # # data_update = combined_data.update(override_data)  # in place
    #
    # # Dictionary unpacking
    # # dict_override = override_data[0]
    #
    # combined_data = default_data.update(dict_override)
    # return combined_data

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


    filepath = 'swapi_planets-v1p0.json'
    filename = 'final.json'



    basic_info = read_json(filepath)


    planet = basic_info[0]
    response = get_swapi_resource(url, {'search': planet['name']})
    planets_results = response[0]['results']

    planet = combine_data(planet, planets_results)
    print(planet)
    planet = filter_data(planet, PLANET_KEYS)

    basic_info = planet

    #print(basic_info)

    write_json(filename, basic_info)

if __name__ == '__main__':
    main()
