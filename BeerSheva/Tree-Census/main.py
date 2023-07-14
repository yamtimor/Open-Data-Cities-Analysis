import streamlit
from get_data import *



if __name__ == "__main__":
    params = load_config()
    base_url = params.get("base_url","")
    api_uri = params.get("api_uri","")
    resource_id = params.get("resource_id","")
    limit = params.get("limit",0)
    records = get_records(base_url,api_uri,resource_id,limit)
    df = record_to_df(records)
    print(df)