import pandas as pd
import requests
import os
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


def get_data(url, resource_id, limit):
    try:
        url = f"{url}?resource_id={resource_id}&limit={limit}"
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

