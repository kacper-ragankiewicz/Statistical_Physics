#!/bin/bash

generated_numbers=1000

echo "Compiling C++ program..."
g++ -std=c++11 cpp/task.cpp -o cpp/exe/task

if [ $? -eq 0 ]; then
    echo "C++ program compiled successfully"

    cpp/exe/task $generated_numbers

    echo "C++ program execution time: ${elapsed_cpp} milliseconds"
else
    echo "Error: Compilation of C++ program failed"
fi
python3 py/task.py $generated_numbers

f/task $generated_numbers
