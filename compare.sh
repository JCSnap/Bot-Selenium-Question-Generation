#!/bin/bash

echo "Running quizwizard.py"
python3 quizwizard.py

echo "Running add_topic_level.py"
python3 add_topic_level.py

echo "Running rolljak.py"
python3 rolljak.py

echo "Running append.py"
python3 append.py

echo "Removing excel"
rm ~/Downloads/excel.xlsx
