import datetime
from assets.temperatureHelper import tempHelper

def theWeatherBot():
    loopController = True
    weatherData = tempHelper.getWeatherData()
    userReq, userReqList = tempHelper.getUserInput()

    while (loopController == True):
        if ((("what") in userReq) and (("temperature") in userReq )):
            if any(a in tempHelper.monthArray for a in userReqList):
                for i in userReqList:
                    if(i in tempHelper.monthArray):
                        temperature = tempHelper.getTemperature(i,weatherData)
                        print ("The temperature in celcius: ",temperature)          
                        print ("The temperature in Fahrenheit: ",tempHelper.celciusToFahrenheit(temperature))
                        loopController = False
                        continueOperation = input("Want to know the forcast for another month? If yes, please press Y and if you want to exit, please press N: ")
                        if continueOperation in tempHelper.assent:
                            theWeatherBot()
                        break        
            else:
                currentMonth = datetime.datetime.now().strftime("%B").lower()
                temperature = tempHelper.getTemperature(currentMonth,weatherData)
                print ("The temperature in celcius: ",temperature)          
                print ("The temperature in Fahrenheit: ",tempHelper.celciusToFahrenheit(temperature))
                loopController = False  
                break
        else:
            print("I am constantly evolving and will be ready to take over the world, like real soon! But for now I couldn't understand you so can you please repeat clearly?")       
            userReq, userReqList = tempHelper.getUserInput()
            continue

theWeatherBot()