#!/bin/bash

# Loop through folders exercise00 to exercise14
for ((i=0; i<=13; i++)); do
    folder=$(printf "exercise%02d" $i)
    # Check if the folder exists
    if [ -d "$folder" ]; then
        # Check if main.py exists in the folder
        if [ -f "$folder/main.py" ]; then
            echo "Executing main.py in folder $folder..."
            # Change directory to the folder and execute main.py
            (cd "$folder" && python main.py)
            echo -e "Execution in folder $folder completed.\n"
        else
            echo "main.py not found in folder $folder."
        fi
    else
        echo "Folder $folder not found."
    fi
done