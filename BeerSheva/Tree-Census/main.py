import streamlit
from get_data import *



if __name__ == "__main__":
    params = load_config()
    url = params.get("url","")
    resource_id = params.get("resource_id","")
    limit = params.get("limit",0)
    data = get_data(url,resource_id,limit)
    records = extract_records(data)
    df = record_to_df(records)
    print(df)