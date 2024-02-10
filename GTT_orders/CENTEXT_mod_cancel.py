

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
                "producttype":"DELIVERY",
                "price":price+1,
                "triggerprice": price,
                "qty":quantity,
                "timeperiod": "20"
                }
    response = obj.gttCreateRule(params)
    return response

rule_id = place_gtt_order(instrument_list,"CENTEXT","BUY",500,10)

# def modify_gtt_order(rule_id,instrument_list,ticker,price,quantity,exchange="NSE"):
#     params = {
#                  "id": rule_id,
#                  "symboltoken": token_lookup(ticker, instrument_list),
#                  "exchange": exchange,
#                  "price": price+1,
#                  "qty": quantity,
#                  "triggerprice": price,
#             }
#     response = obj.gttModifyRule(params)
#     return response

def cancel_gtt_order(rule_id,instrument_list,ticker,exchange="NSE"):
    params = {
                 "id": rule_id,
                 "symboltoken": token_lookup(ticker, instrument_list),
                 "exchange": exchange
            }
    response = obj.gttCancelRule(params)
    return response

# modify_gtt_order(rule_id, instrument_list, "CENTEXT", 550, 5)
cancel_gtt_order(rule_id, instrument_list,"CENTEXT")

# print(modify_gtt_order)
print(cancel_gtt_order)
