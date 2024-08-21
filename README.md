# RealTimeClock

## Overview

The `RealTimeClock` project is a simple Python script that continuously displays the current time in the console, updating every second. It serves as a basic example of how to work with time-related functions in Python and how to create a real-time clock display in a terminal.

## Features

- **Real-Time Clock Display**: The script shows the current time in `HH:MM:SS` format.
- **Console Clear**: Each second, the console is cleared and the time is updated, providing a dynamic and real-time display.
- **Version Check**: The script includes a check to ensure that it's running in Python 3.6 or higher, preventing compatibility issues with older Python versions.

## How It Works

The script uses the following key Python modules and functions:

1. **`sys` Module**:
   - Used to check the version of Python that is running the script. If the version is lower than 3.6, the script will stop execution and provide an error message.

2. **`time` Module**:
   - Provides a `sleep()` function that pauses the execution of the script for one second, allowing the time to update in real-time.

3. **`datetime` Module**:
   - Used to get the current time and format it into a human-readable string.

### Key Code Sections

1. **Version Check**:
   ```python
   if sys.version_info < (3, 6):
       raise RuntimeError("This script requires Python 3.6 or higher. You are using Python {}.{}.{}.".format(
           sys.version_info.major,
           sys.version_info.minor,
           sys.version_info.micro
       ))
