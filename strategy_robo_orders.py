from smartapi import SmartConnect
import os
import urllib
import json
from pyotp import TOTP

key_path = r"D:\OneDrive\Udemy\Angel One API"
os.chdir(key_path)

key_secret = open("key.txt","r").read().split()

obj=SmartConnect(api_key=key_secret[0])
data = obj.generateSession(key_secret[2],key_secret[3],TOTP(key_secret[4]).now())
feed_token = obj.getfeedToken()

instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())

def token_lookup(ticker, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if instrument["name"] == ticker and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[-1] == "EQ":
            return instrument["token"]
        
def get_ltp(instrument_list,ticker,exchange="NSE"):
    params = {
                "tradingsymbol":"{}-EQ".format(ticker),
                "symboltoken": token_lookup(ticker, instrument_list)
             }
    response = obj.ltpData(exchange, params["tradingsymbol"], params["symboltoken"])
    return response["data"]["ltp"]

def place_robo_order(instrument_list,ticker,buy_sell,price,quantity,exchange="NSE"):
    ltp = get_ltp(instrument_list,ticker,exchange)
    params = {
                "variety":"ROBO",
                "tradingsymbol":"{}-EQ".format(ticker),
                "symboltoken":token_lookup(ticker, instrument_list),
                "transactiontype":buy_sell,
                "exchange":exchange,
                "ordertype":"LIMIT",
                "producttype":"BO",
                "duration":"DAY",
                "price":price,
                "stoploss": round(ltp*0.1,1),
                "squareoff": round(ltp*0.2,1),                
                "quantity":quantity
                }
    response = obj.placeOrder(params)
    return response

ltp = get_ltp(instrument_list,"HCLTECH")
place_robo_order(instrument_list, "HCLTECH", "BUY", ltp-10, 1)















