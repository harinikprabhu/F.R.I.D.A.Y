import json
import random

class tempHelper:
    def celciusToFahrenheit(celcius):
        fahrenheit = (9/5) * celcius + 32
        return float("{0:.1f}".format(fahrenheit))

    def getWeatherData():
        with open("assets/weatherInfo.json") as weatherRawData:
            weatherData = json.load(weatherRawData)
        return weatherData

    def getTemperature(i,weatherData):
        temperature = random.uniform(float(weatherData[i]["Coldest"]),float(weatherData[i]["Warmest"]))
        temperatureFormated = float("{0:.1f}".format(temperature))
        return temperatureFormated

    def getUserInput():
        userReq = input("Please ask me for which month you want to know the temperature: ")
        userReqFormated = userReq.lower()
        userReqList = userReqFormated.split(' ')
        return userReqFormated, userReqList

    monthArray = ["january", "february","march","april","may","june","july","august","september","october","november","december"]
    assent = ["yes","YES","Y","Yes","y"]