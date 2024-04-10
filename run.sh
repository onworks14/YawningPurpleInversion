#!/bin/bash

while true; do
    # Ask the user for the day they want to view the answers for
    echo "Please enter the day you want to view the answers for (01-25), or type 'all' to view all answers, or type 'exit' to quit the program:"
    read day

    # Check if the user wants to exit the program
    if [ "$day" == "exit" ]; then
        echo "Exiting the program."
        break
    fi

    # Check if the user wants to view all answers
    if [ "$day" == "all" ]; then
        # Display the contents of result.txt
        cat result.txt && echo -e '\nThanks for reading!' && exit 0
    else
        # Check if the input is a valid day
        if [ "$day" -ge 1 ] && [ "$day" -le 25 ]; then
            # Format the input to ensure days less than 10 have a leading 0
            if [ "$day" -lt 10 ]; then
                day="0$day"
            fi
            # Navigate to the specified day's directory and run main.go
            cd "idol/day$day"
            go run main.go
            # Return to the original directory
            cd ../..
        else
            echo "The entered day is not within the 01-25 range. Please try again."
        fi
    fi

    # Ask the user if they want to continue or exit
    echo "Do you want to continue? (yes/no)"
    read continue_choice
    if [ "$continue_choice" != "yes" ]; then
        echo "Exiting the program."
        break
    fi
done
