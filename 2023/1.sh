#!/bin/bash

# Prompt the user for the day number
echo "Enter the day number in 2023:"
read day

# Check if the day number is valid (assuming days are numbered from 1 to 25)
if (( day < 1 || day > 25 )); then
    echo "Invalid day number. Please enter a number between 1 and 25."
    exit 1
fi

# Navigate to the directory for the specified day
cd "day$day"

# Check if the directory exists
if [ ! -d "$PWD" ]; then
    echo "Directory for day $day does not exist."
    exit 1
fi

# Run the Python scripts for parts 1 and 2
echo "Running scripts for day $day:"
python3 main.py

# Navigate back to the original directory
cd ../..
