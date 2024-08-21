import sys
import time
from datetime import datetime

# Check if the Python version is 3.6 or higher
if sys.version_info < (3, 6):
    raise RuntimeError("This script requires Python 3.6 or higher. You are using Python {}.{}.{}.".format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro
    ))

def display_current_time():
    while True:
        # Get the current time
        now = datetime.now()

        # Format the time as HH:MM:SS
        current_time = now.strftime("%H:%M:%S")

        # Clear the console
        print("\033[2J\033[H", end="")

        # Print the current time
        print("Current Time: ", current_time)

        # Wait for one second before updating the time
        time.sleep(1)

if __name__ == "__main__":
    display_current_time()
