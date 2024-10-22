import random
from time import sleep

# Function to randomly select a gas level from a list
def gasLevelGauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

# Function to randomly select a gas station from a list
def gasStations():
    return random.choice(["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"])

# Function to handle alerts based on gas level
def gasLevelAlert():
    gasLevel = gasLevelGauge()  # Get current gas level
    print(f"\nGas level: {gasLevel}")

    # Dict for messages and distances based on gas level
    messages = {
        "Empty": ("***WARNING - YOU ARE ON EMPTY***\n", "Calling Triple AAA"),
        "Low": ("Your gas tank is extremely low, checking GPS for the closest gas station\n",
                f"The closest gas station is {gasStations()} which is {round(random.uniform(1, 25), 1)} miles away."),
        "Quarter Tank": ("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station\n",
                         f"The closest gas station is {gasStations()} which is {round(random.uniform(25.1, 50), 1)} miles away."),
        "Half Tank": "Your gas tank is half full, which is plenty to get to your destination.",
        "Three Quarter Tank": "Your gas tank is three-quarters full.",
        "Full Tank": "Your gas tank is full!!!"
    }

    # Retrieve and print the corresponding messages based on gas level
    if gasLevel == "Empty":
        print(messages[gasLevel][0])
        sleep(1.5)
        print(messages[gasLevel][1])
    elif gasLevel in ["Low", "Quarter Tank"]:
        print(messages[gasLevel][0])
        sleep(1.5)
        print(messages[gasLevel][1])
    else:
        print(messages[gasLevel])

# Call the function to display the gas level alert
gasLevelAlert()