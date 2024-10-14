print("\n****************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["snowy","blizzard","raining","windy","icy","sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forcast of", weatherAlert, "weather conditions.")

vehicleResponseSystem()