import json

with open('modules/assets/country.json') as json_data:
    d = json.load(json_data)

def countryIterator():
    iterator = input ("Press 1 to continue the Country Info Bot\nPress 2 to go back to main console of F.R.I.D.A.Y\n")
    if iterator == '1':
        country_bot()
    else:
        print("Thank you for using Country Info Bot!")

def country_bot():
    print("You can ask me about location, capital, currency, population, area, population density, GDP, life exp, birth rate and death rate of any country \n\nPlease remember to start the country name with a capital letter \n")
    print("Format: [statistic] of [Country]")
    keyString = input("Please enter your query in the following format: [statistic] of [Country] or just the statistic")

    inputList = keyString.split(" of ")
    try:
        if (len(inputList)==2):
            try:
                information = d[inputList[1]][inputList[0]]
                print (information)
            except KeyError:
                print("Enter a valid query")


        elif (len(inputList) == 1):
            count = 0
            for a in d:
                if count <= 10:
                    print(d[a][inputList[0]])
                    count = count + 1
    except KeyError:
        print ("That is not a valid entry!")
        country_bot()
    countryIterator()