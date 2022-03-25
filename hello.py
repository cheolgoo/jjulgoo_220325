# import requests

# url = "https://api.upbit.com/v1/candles/minutes/1?market=KRW-XRP&count=1"

# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers)

# print(response.text)

# import requests

# url = "https://api.upbit.com/v1/candles/days?count=1"

# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers)

# print(response.text)

# import pyupbit
# df = pyupbit.get_ohlcv("KRW-XRP", interval="minute15", count=5)
# print(df)

# import pyupbit

# orderbook = pyupbit.get_orderbook("KRW-BTC")
# bids_asks = orderbook[1]

# # for bid_ask in bids_asks:
#     print(bid_ask)


import pyupbit
tickers = pyupbit.get_tickers(fiat="KRW")

'''
coin_list = ["KRW-BTC", "KRW-ETH"]

number = 0
for list in coin_list:

 
    coin_data[number] = pyupbit.get_ohlcv(ticker = list)
    number = number + 1
#A = pyupbit.get_ohlcv(ticker = coin_list[0])
#print(A)

'''
# coin_data = pyupbit.get_ohlcv(ticker="KRW-ETH", interval='', count=15000, to=None, period=0.1 )


# open = coin_data['open']
# close = coin_data['close']

# delta = close - open

# i=1
# j=3
# if i==1 and j ==3:
#     print(i)

coin_data = pyupbit.get_ohlcv(ticker="KRW-ETH", interval='minute5', count=15000, to="20210412", period=0.1 )

coin_data.to_excel("5minute_data.xlsx")