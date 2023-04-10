# This script has partial code that is part of the bonus challenge of the lesson. It will use concepts covered in the lesson and avoids going into
# more advanced techniques in Python. The goal is to get you to think about how to use the concepts you have learned in the lesson to solve a problem.
# Use the comments in the code as guidance to complete the challenge.
# Objectives: In this challenge you will need to capture information from files. To do this, you'll mostly use dictionaries.
# Objectives:
# 1. Use the provided code to iterate (loop) over every file in a path (defaults to current directory)
# 2. Capture the file name and the size of the file in a dictionary
# 3. Print out the file name and size of the file in a human readable format sorting from largest to smallest file size

# Note: Run this script on the root of the repository and pass in a path as an argument. For example: `python bonus/main.py /tmp`

import os
import sys

# Path to the directory to iterate over, fallsback to current directory
path = sys.argv[1] if len(sys.argv) > 1 else '.'

# Dictionary to hold the file name and size
file_sizes = {}

# Iterate over the files in the directory
for root, dirs, files in os.walk(path):
    for file in files:
        # Get the full path to the file
        full_path = os.path.join(root, file)

        # Use the os.path.getsize function to get the file size

        # Add the file size to the dictionary

# Modify the following code to print out the file sizes in a human readable format, sorted by largest to smallest
# Note that the current code will only print out the filename and nothing else.
for file in file_sizes:
    print(f"File: {file}")
