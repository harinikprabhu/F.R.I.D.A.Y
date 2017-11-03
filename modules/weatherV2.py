import datetime
import json
import random

with open("assets/weatherInfo.json") as weatherRawData:
            weatherData = json.load(weatherRawData)

loopController = True
monthArray = ["january", "february","march","april","may","june","july","august","september","october","november","december"]
def getUserInput():
    userReq = input("Please enter the month you would like to know the temperature for in correct format: ")
    userReqFormated = userReq.lower()
    userReqList = userReqFormated.split(' ')
    return userReq, userReqList

userReq, userReqList = getUserInput()

while (loopController == True):
    if ((("what") in userReq) and (("temperature") in userReq )):
        if any(a in monthArray for a in userReqList):
            for i in userReqList:
                if(i in monthArray):
                    temperature = random.uniform(float(weatherData[i]["Coldest"]),float(weatherData[i]["Warmest"]))
                    temperatureFormated = float("{0:.1f}".format(temperature))
                    print ("The temperature in celcius: ",temperatureFormated)          
                    print ("The temperature in Fahrenheit: ", ((9/5) * temperatureFormated + 32))
                    loopController = False
                    break  
        else:
            currentMonth = datetime.datetime.now().strftime("%B").lower()
            temperature = random.uniform(float(weatherData[i]["Coldest"]),float(weatherData[i]["Warmest"]))
            temperatureFormated = float("{0:.1f}".format(temperature))
            print ("The temperature in celcius: ",temperatureFormated)          
            print ("The temperature in Fahrenheit: ", float("{0:.1f}".format((9/5) * temperatureFormated + 32)))  
            loopController = False
            break
    else:
        print("My development is still in baby stage! I will be a know-it-all very soon! But for now I couldn't understand you so can you please repeat clearly?")
        userReq, userReqList = getUserInput()
        continue
