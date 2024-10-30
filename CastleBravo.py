print("Welcome to infoTechCenter V1.0")


import time
import sys


# ANSI escape codes for colors
class TextColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m" #Define CYAN color

# Function template for logs
def log(message, level="INFO", color=TextColors.RESET):
    print(f"{color}[{level}] {message}{TextColors.RESET}")

# Individual constants for log levels
LOG_LEVELS = {
    "INFO": (TextColors.GREEN, "INFO"),
    "WARNING": (TextColors.YELLOW, "WARNING"),
    "ERROR": (TextColors.RED, "ERROR"),
}

# `log` wrapper to use the color library for easy calling
def log_message(level, message):
    color, level_str = LOG_LEVELS.get(level, (TextColors.RESET, "INFO"))
    log(message, level=level_str, color=color)

# Loop to simulate the event-logging process
for i in range(5):
    if i == 0:
        log_message("INFO", "Process started")
    elif i == 3:
        log_message("WARNING", "CPU usage is high")
    elif i == 4:
        log_message("ERROR", "Process failed")
    else:
        log_message("INFO", f"Running iteration {i}")

# Reset display cursor after running a test
print(TextColors.RESET, end="")
# Initialize counters for the boot process
x = 0  # Counter for booting iterations
ellipsis = 0  # Counter for the ellipsis effect

timetosleep = 4  # variable to set the time library to 4 seconds when called
time.sleep(timetosleep)  # calling the time to sleep library with the variable time

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the boot counter
    # Create a booting message with an ellipsis effect and cyan color
    message = f"{TextColors.CYAN}InfoTech Center System Booting" + "." * ellipsis + f"{TextColors.RESET}"
    ellipsis += 1  # Increment the ellipsis counter
    sys.stdout.write("\r" + message)  # Overwrite the current line with the message
    time.sleep(0.2)  # Pause for half a second

    # Reset ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0

# Check if the boot process is complete
if x == 20:
    # Green color for the final success message
    print(f"\n{TextColors.GREEN}Operating System Booted Up - Retina Scanned - Access Granted{TextColors.RESET}")

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
