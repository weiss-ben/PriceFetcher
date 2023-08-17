# Price Fetcher

## 1. Install polygon.io REST API and Set up API Key

### 1.1 Install REST API

'''pip install -U polygon-api-client'''

### 1.2

Download the API key and place it in ./config/api.config.JSON

## 2. Create a GC Project and set up the Google Cloud CLI

### 2.1 Set up a service account to acces the project from source code
https://docs.openbridge.com/en/articles/1856793-how-to-set-up-google-bigquery-creating-and-configuring-service-accounts-in-google-cloud-console

Download the Service account JSON file and place it in ./config

### 2.2 Set up a connection from python to GCP/BigQuery
https://hex.tech/blog/connecting-bigquery-python/?utm_id=h_7015f000000VLkDAAW&utm_campaign=hexcontent&utm_medium=social%20media&utm_source=reddit

## 3. Create the BigQuery data environment

### 3.1 Create the price_data data set

### 3.2 Create the DailyPriceData table

Copy the code from ./sql/create_price.sql to the BigQuery SQL workbench and execute to create the table

## 4. Run PriceFetcher

from the PriceFetcher directory, execute:
'''py ./main.py'''

Make sure to execute *during or after market hours*, otherwise an error will occur