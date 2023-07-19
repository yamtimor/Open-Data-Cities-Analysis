import pandas as pd
import requests
import os
import yaml
import json

def load_config():
    """
    Load configuration
    :return: configuration
    """

    if os.path.isfile('config.yaml'):
        with open('config.yaml', 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
    else:
        config = {}
    return config


def get_records(base_url, api_uri, resource_id, limit):
    """
    Get records from API
    :param base_url: Base URL of API
    :param api_uri: URI of API
    :param resource_id: ID of the resource
    :param limit: 1000
    :return: records
    """

    records = list()
    try:
        url = f"{base_url}{api_uri}?resource_id={resource_id}&limit={limit}"
        response = requests.get(url)
        data = response.json()
        counter = 1
        while len(data['result']['records']) != 0:
            if response.ok:
                print(f"running batch {counter}")
                counter += 1 # increment counter
                records += data['result']['records']
            else:
                print("got invalid response")

            response = requests.get(f'{base_url}{data["result"]["_links"]["next"]}')
            data = response.json()

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    return records


def record_to_df(records):
    """
    Convert records to dataframe
    :param records: records
    :return: dataframe
    """

    if records is None:
        return None
        print("records is None")

    else:
        df = pd.DataFrame(records)
        return df
        print("return dataframe")