# Price Fetcher

## 1. Install polygon.io REST API
'''pip install -U polygon-api-client'''

## 2. Create a GC Project and set up the Google Cloud CLI

### 2.1 Set up a service account to acces the project from source code
https://docs.openbridge.com/en/articles/1856793-how-to-set-up-google-bigquery-creating-and-configuring-service-accounts-in-google-cloud-console

### 2.2 Set up a connection from python to GCP/BigQuery
https://hex.tech/blog/connecting-bigquery-python/?utm_id=h_7015f000000VLkDAAW&utm_campaign=hexcontent&utm_medium=social%20media&utm_source=reddit

## 3. Create the BigQuery data environment
### 3.1 Create the price_data data set
### 3.2 Create the DailyPriceData table