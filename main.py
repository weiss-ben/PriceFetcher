########################
##### Dependencies #####
########################

# Stock data REST client
from polygon import RESTClient

# JSON for reading config files
import json

# Datetime for api querying
import datetime

# GCS writing
import GCS_module

############################
###### API Connetction #####
############################

# Get API key from config
with open('./config/api.config.JSON', 'r') as api_file:
    api_key = json.load(api_file)

# Establish API connection
client = RESTClient(api_key['key'])

#############################
##### DB/GCS Connection #####
#############################

#############################
##### Ticker/Price info #####
#############################

# Load list of tickers from config file
with open('./config/ticker_list.config.JSON', 'r') as ticker_file:
    tickers = json.load(ticker_file)

# Today's date for API queries
today = str(datetime.date.today())

# Query each ticker and load into DB
for t in tickers['tickers']:
    # Query API
    request = client.get_daily_open_close_agg(
        t,
        today,
    )

    # Insert price into DB
    GCS_module.write_read('bucket_name_here', 'blob_name_here', request)
    print('ticker: ', request.symbol, ' close: ', request.close, request)
