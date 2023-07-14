import pandas as pd
import streamlit
import requests
import os
from pprint import pprint


def get_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    url = "https://data.gov.il/api/3/action/datastore_search?resource_id=b7bfe395-a977-452a-8429-e258b71c5b10&limit=5"
    data = get_data(url)
    pprint(data['result']['records'])