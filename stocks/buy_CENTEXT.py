from smartapi import SmartConnect
import pyotp
import urllib
import json



obj = SmartConnect(api_key="0")
data = obj.generateSession("0", pyotp.TOTP("").now())


instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())

refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)


# to place order
try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "CENTEXT-EQ",
        "symboltoken": "11511",
        "transactiontype": "BUY",
        "exchange": "NSE",
        "ordertype": "LIMIT",
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": "19500",
        "squareoff": "0",
        "stoploss": "0",
        "quantity": "1"
        }
    orderId=obj.placeOrder(orderparams)
    print("The order id is: {}".format(orderId))
except Exception as e:
    print("Order placement failed: {}".format(e.message))

print(orderparams)