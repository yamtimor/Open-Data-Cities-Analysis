import streamlit
from get_data import *


if __name__ == "__main__":
    url = "https://data.gov.il/api/3/action/datastore_search?resource_id=b7bfe395-a977-452a-8429-e258b71c5b10&limit=5"
    data = get_data(url)
    records = extract_records(data)
    df = record_to_df(records)
    print(df)