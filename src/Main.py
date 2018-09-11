import requests

r = requests.get('https://api.iextrading.com/1.0/stock/aapl/earnings')
print(r.status_code)
print(r.json())