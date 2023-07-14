import pandas as pd
import streamlit
import requests
import os


# +
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

get_data()