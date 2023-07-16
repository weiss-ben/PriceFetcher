# Import REST client
from polygon import RESTClient

# import JSON for reading config files
import json

###### API Connetction #####

# Get API key from config
with open('api.config.JSON', 'r') as api_file:
    api_key = json.load(api_file)

# Establish API connection
client = RESTClient(api_key['key'])

##### DB Connection #####

##### Ticker/Price info #####

# Load list of tickers from config file
with open('ticker_list.config.JSON', 'r') as ticker_file:
    tickers = json.load(ticker_file)

# Query each ticker and load into DB
for t in tickers['tickers']:
    # Query API
    request = client.get_daily_open_close_agg(
        t,
        '2023-07-14',
    )

    # Insert price into DB
    print(request)
