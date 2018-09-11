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
        print(r)
        parseResults(r)
        count = 0
        requrl = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
    requrl = requrl + stock['symbol'] + ','
    count += 1

requrl = requrl + '&types=quote,stats'
r = requests.get(requrl).json()
print(r)
parseResults(r)


print(result)

# def getPBV(symbol):
#     r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/stats").json()
#     return r['priceToBook']
#
#
# def getPE(symbol):
#     r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/book").json()
#     return r['quote']['peRatio']
#
#
# # Iterate through each stock and calculate the P/E * P/BV value
# # If it is below 22.5, add it to result list
# for stock in listStocks:
#     stockSymbol = stock['symbol']
#     print('starting execution for ' + stockSymbol)
#     stockName = stock["name"]
#     stockPE = getPE(stockSymbol)
#     if stockPE is None:
#         continue
#     stockPBV = getPBV(stockSymbol)
#     if stockPBV is None:
#         continue
#     val = stockPE * stockPBV
#     if val <= 22.5:
#         result.append({"symbol": stockSymbol, "name": stockName, "val": val})
#
# print(result)
