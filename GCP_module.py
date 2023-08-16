from google.cloud import bigquery
from google.oauth2 import service_account

# Set up authenticated project access
credentials = service_account.Credentials.from_service_account_file('.\config\price-fetcher-395923-7ff04b88fd66.json')
project_id = 'price-fetcher-395923'  
bq_client = bigquery.Client(credentials=credentials, project=project_id)

# Insert into Price Table
def insert_price_table(rows_to_insert):
    table_id = 'price-fetcher-395923.price_data.DailyPriceData'

    errors = bq_client.insert_rows_json(table_id, rows_to_insert)