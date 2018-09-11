import requests

# Initialize result list
result = []


def parseResults(json):
    for stock in json:
        stock = json[stock]
        PE = stock['quote']['peRatio']
        if PE is None:
            continue
        PBV = stock['stats']['priceToBook']
        if PBV is None:
            continue
        if PE * PBV <= 22.5:
            result.append({'symbol': stock['quote']['symbol'],
                           'name': stock['quote']['companyName'],
                           'value': PE * PBV})


# Get list of symbols supported by IEX and parse it into JSON format
r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
listStocks = r.json()

# Create batch request url
requrl = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
count = 0
for stock in listStocks:
    if count == 1499:
        requrl = requrl + '&types=quote,stats'
        r = requests.get(requrl).json()
        parseResults(r)
        count = 0
        requrl = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
    requrl = requrl + stock['symbol'] + ','
    count += 1

requrl = requrl + '&types=quote,stats'
r = requests.get(requrl).json()
parseResults(r)


print(result)