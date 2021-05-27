import requests as re
import pandas as pd

def load_data_api1(data_dict):
    response1 = re.get('https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/rand-registry-prices/')    
    data = response1.json()

    addresses = []
    cities = []
    dates = []
    prices = []

    """Extracting only the relavant bits of data from the json object
    """
    for addr in data['results']:        
        addresses.append(addr['address'])
        cities.append(addr['city'])
        dates.append(addr['date'])
        prices.append(addr['price'])

    
    """Prepare a dictionary in order to turn it into a pandas dataframe below
    """
    data_dict = {
        "address": addresses,
        "city": cities,
        "date": dates,
        "price": prices
    }

    return data_dict    



def convert_dict_dif(data_dict):
    """ Convert python dictionary to pandas dataframe
    """
    return pd.DataFrame.from_dict(data_dict)

def load_data_api2(data):    
    response2 = re.get('https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/random-price-index')
    data = response2.json()

    cities = []
    dates = []
    prices= []

    for avg in data['results']:
        cities.append(avg['city'])
        dates.append(avg['date'])
        prices.append(avg['price'])

    data2_dict = {
        "city" : cities,
        "date": dates,
        "price": prices
    }

    return data2_dict

def replace_city_code(df_data2_dict):

    city_code = {
    "S00": "HILL VALLEY",
    "S01": "MOS EISLEY",
    "S02": "PAWNEE", 
    "S03": "ANKH-MORPORK",
    "S04": "LIBERTY CITY",
    "S05": "DUCKBURG",
    "S06": "BEDROCK"
}
    df_data2_dict['city'] = df_data2_dict['city'].replace(city_code)

    return df_data2_dict


    
    
