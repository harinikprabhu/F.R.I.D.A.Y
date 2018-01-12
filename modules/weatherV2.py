import datetime
import json
import random

with open("modules/assets/weatherInfo.json") as weatherRawData:
            weatherData = json.load(weatherRawData)

loopController = True
monthArray = ["january", "february","march","april","may","june","july","august","september","october","november","december"]

def weatherIterator():
    iterator = input("Press 1 to continue the Weather Info Bot\nPress 2 to go back to main console of F.R.I.D.A.Y\n")
    if iterator == '1':
        global loopController
        loopController = True
        weatherBot()
    else:
        print("Thank you for using Weather Info Bot!")

def weatherBot():
    def getUserInput():
        userReq = input("Please enter the month you would like to know the weather in the format 'what is the weather in {month}': \n")
        userReqFormated = userReq.lower()
        userReqList = userReqFormated.split(' ')
        return userReq, userReqList

    userReq, userReqList = getUserInput()
    global loopController
    while (loopController == True):
        if ((("what") in userReq) and (("weather") in userReq )):
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
            print("\nPlease enter the query in the format 'what is the temperature in {month}'")
            userReq, userReqList = getUserInput()
            continue
    weatherIterator()
