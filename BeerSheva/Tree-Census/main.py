from get_data import *
from heatmap import create_heatmap

def main():

    # Trees data pipeline
    params = load_config()
    base_url = params.get("base_url","")
    api_uri = params.get("api_uri","")
    resource_id = params.get("resource_id","")
    limit = params.get("limit",0)
    records = get_records(base_url, api_uri, resource_id, limit)
    df = record_to_df(records)
    print(df)




if __name__ == "__main__":
    main()
