from modules.calculator import calculator_main
from modules.weatherV2 import weatherBot
from modules.country import country_bot

print ("Hello! My name is F.R.I.D.A.Y, a bot. I can transform into a Calculator, Weather Info Bot or a Country Info Bot!")

def fridayIterator():
    iterator = input("Would you like to continue using F.R.I.D.A.Y? \nPress Y to continue or\nPress N to Exit \n")
    if iterator in ['Y', 'y']:
        FRIDAY()
    elif iterator in ['N', 'n']:
        print ("'kay, bye! I'm off to take over the world!")

def FRIDAY():
    selector = input ("Press 1 if you want a Calculator \nPress 2 if you want a Weather Info Bot \nPress 3 if you want a Country Info Bot\nPress 4 to exit F.R.I.D.A.Y\n")
    if selector == '1':
        calculator_main()
        fridayIterator()
    elif selector == '2':
        weatherBot()
        fridayIterator()
    elif selector == '3':
        country_bot()
        fridayIterator()
    elif selector == '4':
        print("Okay, bye! I'm off to take over the world!")

FRIDAY()


