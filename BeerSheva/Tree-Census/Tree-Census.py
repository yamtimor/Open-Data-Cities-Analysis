import pandas as pd
import streamlit
import requests
import os
from pprint import pprint
import yaml

def load_config():
    if os.path.isfile('config.yaml'):
        with open('config.yaml', 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
    else:
        config = {}
    return config


def get_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def extract_records(data):
    return data['result']['records']

def record_to_df(records):
    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    url = "https://data.gov.il/api/3/action/datastore_search?resource_id=b7bfe395-a977-452a-8429-e258b71c5b10&limit=5"
    data = get_data(url)
    records = extract_records(data)
    df = record_to_df(records)
    print(df)