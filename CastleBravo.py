print("\n****************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["snowing","blizzard","raining","windy","icy","sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

print(weather())