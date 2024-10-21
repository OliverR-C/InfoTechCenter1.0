print("\n****************************************\n")  # Decorative line for separation

print("Weather Branch\n")  # Title of the system

# Import Libraries
import random  # Randomly select weather conditions
from time import sleep  # Simulate delay in response

# Function to simulate weather forecast
def weather():
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]
    return random.choice(weatherForecast)  # Randomly select a condition

# Get the current weather condition
weatherAlert = weather()

# Function to simulate vehicle response based on weather conditions
def vehicleResponseSystem():
    # Create a dictionary to store the delays and speed limits for each weather condition
    weatherData = {
        "snowy": (30, 55),
        "blizzard": (45, 45),
        "rainy": (15, 65),
        "windy": (5, 70),
        "icy": (50, 30),
    }

    # Check if weather condition is in the dictionary (hazardous weather)
    if weatherAlert in weatherData:
        delay, speed = weatherData[weatherAlert]  # Get the delay and speed limit
        print(f"\nThe National Weather Service has updated our alarm by {delay} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")  # Display updated alarm time
        sleep(1)  # Simulate delay
        print(f"\nVRS system has been engaged only allowing you to drive {speed}mph.")  # Display speed limit
    else:
        # For non-hazardous weather (e.g., sunny)
        print(f"\nThe NWS is calling for {weatherAlert} skies, drive carefully to get to your destination!")  # No delay needed
        sleep(1)  # Simulate delay
        print("\nVRS system has been disengaged.")  # VRS disengaged, no speed restrictions

# Call the function to simulate the vehicle's response based on the weather condition
vehicleResponseSystem()