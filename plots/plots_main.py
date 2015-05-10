# Name: 	plots_main.py
# Author: 	Pan Ding
# Date: 	May 08, 2015
# Summary:	The main program, which does three things
#			1) It loads the csv file into a dataframe and cleans the data.
#			2) Then it asks the user to input a Borough name, and plots the volume of complaints for each agency in this Borough. It stops until the user enters 'finish'.
#			3) Then it asks the user to input an agency name, and plots the volume of complaints for this agency in each Borough. It stops until the user enters 'finish'.
########################################################################################## 

import pandas as pd
import matplotlib.pyplot as plt

import load_clean_data as lcd
import user_input as ui
import draw_plots as dp


if __name__ == "__main__":

	#### Loads and cleans data####
	df_raw = lcd.dataframe().load_csv() 
	df = lcd.clean_df(df_raw)

	#### Draws bar plots for given Boroughs ####
	boroughs = list(df.Borough.unique())
	boroughs.remove('Unspecified')
	boroughs.append('NYC')
	while True:
		boro = ui.get_borough(boroughs) # gets input from user
		if boro == 'FINISH':
			break						# exit the interactiove mode
		else:
			dp.draw_boro_bar(df, boro)			

	#### Draws pie plots for given agencies ####
	agencies = list(df.Agency.unique())
	while True:
		agency = ui.get_agency(agencies) # gets the input from user
		if agency =="FINISH":
			break                        # exit the interactiove mode
		else:			
			dp.draw_agency_pie(df, agency)




