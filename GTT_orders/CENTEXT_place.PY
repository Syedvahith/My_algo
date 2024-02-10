

from smartapi import SmartConnect
import urllib
import json
import pyotp


obj = SmartConnect(api_key="")
data = obj.generateSession("", pyotp.TOTP("").now())
refreshToken = data["data"]['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)


instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())

def token_lookup(ticker, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if instrument["name"] == ticker and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[-1] == "EQ":
            return instrument["token"]

def place_gtt_order(instrument_list,ticker,buy_sell,price,quantity,exchange="NSE"):
    params = {
                "tradingsymbol":"{}-EQ".format(ticker),
                "symboltoken":token_lookup(ticker, instrument_list),
                "transactiontype":buy_sell,
                "exchange":exchange,
                "producttype":"DELIVERY", #only DELIVERY and MARGIN acceptable
                "price":price + 1,
                "triggerprice": price,
                "qty":quantity,
                "timeperiod": "20" #number of days to expiry. Max value 365
                }
    response = obj.gttCreateRule(params)
    return response
place_gtt_order(instrument_list, "CENTEXT", "BUY", 500, 10)
print(token_lookup)
print("---------------------------------")
print(place_gtt_order)


