from smartapi import SmartConnect
import pyotp 


obj = SmartConnect(api_key="")
data = obj.generateSession(", pyotp.TOTP("").now())
refreshToken = data["data"]['refreshToken']
 
#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)


feedToken = obj.getfeedToken()
print(feedToken)
print(userProfile)