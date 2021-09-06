from binance import Client   
from time import sleep
from binance import ThreadedWebsocketManager
import pandas as pd


############################# initiations ########################################


api_key = "enter your key here"
api_secret ="enter your key here"


client = Client(api_key,api_secret)
print("successfully connected")

#print(client.get_historical_klines("BTCUSDT","1m","30 m ago UTC"))
#######################################################################



#buy_order = client.futures_create_order(symbol='BTCUSDT', side='BUY', type='MARKET', quantity=0.001)


btc_price = {'error':False}

def btc_trade_history(msg):
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
        btc_price['error'] = False
    else:
        btc_price['error'] = True

bsm = ThreadedWebsocketManager()
bsm.start()
bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
bsm.stop
