import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_location_name():
    return __locations

def get_artifacts():
    print("Loading....")
    global __locations
    global __data_columns
    with open('../columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open('../banglore_home_prices_model.pickle') as f:
        __model = pickle.load(f)

if __name__ == "__main__":
    get_artifacts()
    print(get_location_name())