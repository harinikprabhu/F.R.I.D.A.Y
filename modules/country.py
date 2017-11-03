import json

with open('assets/country.json') as json_data:
    d = json.load(json_data)

keyString = input("Please enter what you need to know in the following format \
{Field} of {Country} or enter just the {field}\
 to get the summarized country details: ")

inputList = keyString.split(" of ")

if (len(inputList)==2):
    information = d[inputList[1]][inputList[0]]
    print (information)
elif (len(inputList) == 1 ):
    count = 0
    for a in d:
        if count <= 10:
            print(d[a][inputList[0]])
            count = count + 1