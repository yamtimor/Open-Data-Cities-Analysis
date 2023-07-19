import streamlit
from get_data import *

def main():

    # Trees data pipeline
    params = load_config()
    Trees_base_url = params.get("base_url","")
    Trees_api_uri = params.get("api_uri","")
    Trees_resource_id = params.get("resource_id","")
    limit = params.get("limit",0)
    records = get_records(Trees_base_url, Trees_api_uri, Trees_resource_id, limit)
    df = record_to_df(records)
    print(df)

    #



if __name__ == "__main__":
    main()
