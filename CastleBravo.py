print("\n****************************************\n")  # Prints a decorative line for separation

print("Weather Branch\n")  # Prints the title of the system

# Import Libraries Here
import random  # Import random library to select random weather conditions
from time import sleep  # Import sleep function to simulate delay in response


# Function to simulate weather forecast
def weather():
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]
    # Randomly choose one condition from the list
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


# Get the current weather condition
weatherAlert = weather()


# Function to simulate vehicle response based on weather conditions
def vehicleResponseSystem():
    # Check if the weather condition is snowy
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Adjust alarm by 30 minutes
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 55mph.")  # Limit speed to 55 mph

    # Check if the weather condition is a blizzard
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Adjust alarm by 45 minutes
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 45mph.")  # Limit speed to 45 mph

    # Check if the weather condition is rainy
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Adjust alarm by 15 minutes
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 65mph.")  # Limit speed to 65 mph

    # Check if the weather condition is windy
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Adjust alarm by 5 minutes
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 70mph.")  # Limit speed to 70 mph

    # Check if the weather condition is icy
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Adjust alarm by 50 minutes
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 30mph.")  # Limit speed to 30 mph

    # If it's sunny or other non-hazardous conditions
    else:
        print("\nThe NWS is calling for", weatherAlert,
              "skies, drive carefully to get to your destination!")  # No delay needed
        sleep(1)  # Simulate delay
        print("\nVRS system has been disengaged.")  # VRS disengaged, no speed restrictions


# Call the function to simulate the vehicle's response based on the weather condition
vehicleResponseSystem()