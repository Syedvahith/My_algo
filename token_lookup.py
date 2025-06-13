from smartapi import SmartConnect
import pyotp
import urllib
import json
import pandas as pd
import datetime as dt



obj = SmartConnect(api_key="Your key")
data = obj.generateSession(, pyotp.TOTP("").now())


instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())

refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)
#print(instrument_list)



def token_lookup(ticker, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if instrument["name"] == ticker and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[-1] == "EQ":
            return instrument["token"]
        
def symbol_lookup(token, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if instrument["token"] == token and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[-1] == "EQ":
            return instrument["name"]


def hist_data(tickers,duration,interval,instrument_list,exchange="NSE"):
    hist_data_tickers = {} 
    for ticker in tickers:
        params = {
                 "exchange": exchange,
                 "symboltoken": token_lookup(ticker,instrument_list),
                 "interval": interval,
                 "fromdate": (dt.date.today() - dt.timedelta(duration)).strftime('%Y-%m-%d %H:%M'),
                 "todate": dt.date.today().strftime('%Y-%m-%d %H:%M')  
                 }
        hist_data = obj.getCandleData(params)
        df_data = pd.DataFrame(hist_data["data"],
                               columns = ["date","open","high","low","close","volume"])
        df_data.set_index("date",inplace=True)
        df_data.index = pd.to_datetime(df_data.index)
        df_data.index = df_data.index.tz_localize(None)
        hist_data_tickers[ticker] = df_data
    return hist_data_tickers

candle_data = hist_data(["IDEA","CENTEXT", "PATELENG"], 50, "ONE_HOUR", instrument_list) 

print(token_lookup)


candle_data = hist_data(["IDEA","CENTEXT", "PATELENG"], 50, "ONE_HOUR", instrument_list) 

# Call the token_lookup function to retrieve the symbol token for a ticker
idea_token = token_lookup("IDEA", instrument_list)
centext_token = token_lookup("CENTEXT", instrument_list)
pateleng_token = token_lookup("PATELENG", instrument_list)
print("Symbol Token for IDEA:", idea_token)
print("Symbol Token for centext:", centext_token)
print("Symbol Token for pateleng:", pateleng_token)
