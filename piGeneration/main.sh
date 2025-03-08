#!/bin/bash

generated_numbers=100000

echo "Do you want to run the program in C++, Python, or Fortran? (Enter 'C' for C++, 'P' for Python, and 'F' for Fortran)"
read choice

if [ "$choice" == "C" ] || [ "$choice" == "c" ]; then
    # Ask the user if they want to change generated numbers
    echo "Do you want to change the generated numbers? (Enter 'y' or 'n')"
    read change_numbers

    if [ "$change_numbers" == "y" ]; then
        # Ask the user for input of generated numbers
        while true; do
            echo "Enter the generated numbers (separated by spaces, not bigger than 1000000):"
            read generated_input

            # Check if the input is numeric, use custom generated numbers, otherwise use default
            if [[ "$generated_input" =~ ^[0-9]+$ ]] && [ "$generated_input" -le 1000000 ]; then
                generated_numbers=$generated_input
                break
            elif [ "$generated_input" == "n" ]; then
                break
            else
                echo "Error: Invalid input. Please enter a numeric value not bigger than 1000000 or 'n' for default. Please try again."
            fi
        done
    fi

    # Compile the C++ program and pass the generated numbers as command-line arguments
    g++ -std=c++11 cpp/task.cpp -o cpp/exe/task
    if [ $? -eq 0 ]; then
        echo "C++ program compiled successfully"
        # Execute the C++ program with the user input as command-line arguments
        cpp/exe/task $generated_numbers
        if [ $? -eq 0 ]; then
            echo "C++ program executed successfully"
            # Run the Python plotting script
            python3 py/plot.py "C++ chart" data/pi_values.dat
            if [ $? -eq 0 ]; then
                echo "Python script executed successfully"
            else
                echo "Error: Failed to execute the Python script"
            fi
        else
            echo "Error: Failed to execute the C++ program"
        fi
    else
        echo "Error: Compilation of C++ program failed"
    fi
elif [ "$choice" == "P" ] || [ "$choice" == "p" ]; then
    # Ask the user if they want to change generated numbers
    echo "Do you want to change the generated numbers? (Enter 'y' or 'n')"
    read change_numbers

    if [ "$change_numbers" == "y" ]; then
        # Ask the user for input of generated numbers
        while true; do
            echo "Enter the generated numbers (separated by spaces, not bigger than 1000000):"
            read generated_input

            # Check if the input is numeric, use custom generated numbers, otherwise use default
            if [[ "$generated_input" =~ ^[0-9]+$ ]] && [ "$generated_input" -le 1000000 ]; then
                generated_numbers=$generated_input
                break
            elif [ "$generated_input" == "n" ]; then
                break
            else
                echo "Error: Invalid input. Please enter a numeric value not bigger than 1000000 or 'n' for default. Please try again."
            fi
        done
    fi

    # Run the Python script with the user input as command-line arguments
    python3 py/task.py $generated_numbers
    if [ $? -eq 0 ]; then
        echo "Python script executed successfully"
        # Run the Python plotting script
        python3 py/plot.py "Python chart" data/pi_values.dat
        if [ $? -eq 0 ]; then
            echo "Python script executed successfully"
        else
            echo "Error: Failed to execute the Python script"
        fi
    else
        echo "Error: Failed to execute the Python script"
    fi

    elif [ "$choice" == "F" ] || [ "$choice" == "f" ]; then
    # Ask the user if they want to change generated numbers
    echo "Do you want to change the generated numbers? (Enter 'y' or 'n')"
    read change_numbers

    if [ "$change_numbers" == "y" ]; then
        # Ask the user for input of generated numbers
        while true; do
            echo "Enter the generated numbers (separated by spaces, not bigger than 1000000):"
            read generated_input

            # Check if the input is numeric, use custom generated numbers, otherwise use default
            if [[ "$generated_input" =~ ^[0-9]+$ ]] && [ "$generated_input" -le 1000000 ]; then
                generated_numbers=$generated_input
                break
            elif [ "$generated_input" == "n" ]; then
                break
            else
                echo "Error: Invalid input. Please enter a numeric value not bigger than 1000000 or 'n' for default. Please try again."
            fi
        done
    fi

    # Compile and run the Fortran program
    gfortran f/task.f90 -o f/task
    if [ $? -eq 0 ]; then
        echo "Fortran program compiled successfully"
        # Execute the Fortran program with the user input as command-line arguments
        f/task $generated_numbers
        if [ $? -eq 0 ]; then
            echo "Fortran program executed successfully"

            python3 py/plot.py "Fortran chart" data/$generated_numbers
            if [ $? -eq 0 ]; then
                echo "Python script executed successfully"
            else
                echo "Error: Failed to execute the Python script"
            fi
        else
            echo "Error: Failed to execute the Fortran program"

        python3 py/plot.py "Fortran chart" data/$generated_numbers
            if [ $? -eq 0 ]; then
                echo "Python script executed successfully"
            else
                echo "Error: Failed to execute the Python script"
            fi
        fi
    else
        echo "Error: Compilation of Fortran program failed"
    fi
else
    echo "Invalid choice. Please enter 'C' for C++, 'P' for Python, or 'F' for Fortran."
fi

