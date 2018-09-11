import requests

# Initialize result list
result = []
# Set base path for API calls
baseURL = 'https://api.iextrading.com/1.0'


# Given a list of stocks with quotes and stats being retrieved from IEX API,
# add any stocks that have a P/E * P/BV value of 22.5 or less to the result list
def parseResults(json):
    for stock_info in json:
        stock_info = json[stock_info]
        pe = stock_info['quote']['peRatio']
        if pe is None:
            continue
        pbv = stock_info['stats']['priceToBook']
        if pbv is None:
            continue
        if pe * pbv <= 22.5:
            result.append({'symbol': stock_info['quote']['symbol'],
                           'name': stock_info['quote']['companyName'],
                           'value': pe * pbv})


# Get list of symbols supported by IEX and parse it into JSON format
listStocks = requests.get(baseURL + '/ref-data/symbols').json()

# Create batch request url
request_url = baseURL + '/stock/market/batch?symbols='
count = 0
# Iterate through each stock and add it to batch url
# Adding every stock results in 414 so requests are sent out
# in batches of 1500
for stock in listStocks:
    if count == 1499:
        request_url = request_url + '&types=quote,stats'
        r = requests.get(request_url).json()
        parseResults(r)
        count = 0
        request_url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
    request_url = request_url + stock['symbol'] + ','
    count += 1

request_url = request_url + '&types=quote,stats'
r = requests.get(request_url).json()
parseResults(r)

print(result)
