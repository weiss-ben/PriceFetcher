from google.cloud import bigquery
from google.oauth2 import service_account 
import json

# Set up authenticated project access
credentials = service_account.Credentials.from_service_account_file('.\config\price-fetcher-395923-f2da24241920.json')
project_id = 'price-fetcher-395923'  
client = bigquery.Client(credentials=credentials, project=project_id)

# Insert into Price Table
def insert_price_table():
    query = client.query("""INSERT a, b, c INTO table name here""")
    client.query(query)
    
def write_read(bucket_name, blob_name, request):
    """Write and read a blob from GCS using file-like IO"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Mode can be specified as wb/rb for bytes mode.
    # See: https://docs.python.org/3/library/io.html
    with blob.open("w") as f:
        # Write ticker as JSON
        temp = {
            'ticker' : request.symbol,
            'price' : request.close,
            'date' : request.from_
        }
        json.dumps(temp)

        f.write(temp)

    f.close()
