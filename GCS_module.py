from google.cloud import storage
import json

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

    with blob.open("r") as f:
        print(f.read())

    f.close()
