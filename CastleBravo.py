# Print header information
print("\n*********************************\n")
print("Gasoline Branch\n")

# Import required modules
import random  # Used to randomly choose gas level and gas station
from time import sleep  # Used to introduce delays in the program


# Function to randomly select a gas level from a list
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)  # Randomly return one of the gas levels


# Function to randomly select a gas station from a list
def gasStations():
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)  # Randomly return one of the gas stations


# Function to provide alerts based on the current gas level
def gasLevelAlert():
    # Generate random distances to the nearest gas station for "Low" and "Quarter Tank"
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Distance for Low gas level (1 to 25 miles)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)  # Distance for Quarter Tank (25.1 to 50 miles)

    gasLevelIndicator = gasLevelGauge()  # Get current gas level

    # Check the gas level and provide corresponding alerts
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(1.5)  # Wait for 1.5 seconds before the next message
        print("Calling Triple AAA")  # Simulate calling for roadside assistance
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station\n")
        sleep(1.5)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station\n")
        sleep(1.5)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarter tanks full.")
    else:
        print("Your gas tank is full!!!")


# Call the gasLevelAlert function to run the program
gasLevelAlert()