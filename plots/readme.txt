1. plots_main.py
The main program loads the csv file into a dataframe and cleans the data.

Then it asks the user to input a Borough name, and plots the volume of complaints for each agency in this Borough. It stops until the user enters 'finish'.

Then it asks the user to input an agency name, and plots the volume of complaints for this agency in each Borough. It stops until the user enters 'finish'.


2. load_clean_data.py
This module defines a class to load the csv file to a dataframe and eliminates the irrelavant columns.

It also defines a function that cleans the dataframe. 


3. dataframe.py
This module defines two functions to get input from the user. The functions will continue to ask for input until it gets a valid one. "Ctrl+C" will exit the main program.


4. draw_plots.py
This module contains two functions. One draws a bar plot for a given Borough. The other draws a pie plot for a given agency.
