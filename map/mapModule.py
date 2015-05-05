####################################################################################################
#
#
#	Author : Liwen Tian(tl1759)
#	DS GA 1007
#	Final Project
#
#	
#
####################################################################################################



import csv
import sys
import shapefile
import pandas as pd
import numpy as np
from cleanupdata import *
from plotdata import *
from userinput import *
from prompt import *
if __name__ == '__main__':
	print "Now it's loading the data and it may take some time, thank you for your patience!"
	try:
	#Read in the complaintsdata 
		complaintsdata = pd.read_csv('311_data_2014_clean.csv',low_memory = False)
		zipcodedata = pd.read_csv('zip_borough.csv') #load zipcode data with pandas
		dat = shapefile.Reader('tl_2013_us_zcta510')# load shapefile
		zipBorough = getzipBorough(zipcodedata)
		k  = plotMaps(zipBorough)
	except IOError:
		raise Exception("Please make sure all the files in the same folder.")
		sys.exit()
	except KeyboardInterrupt:
		print ('You have touch the keyboard!')
		quitproject()
	i = True
	while (i == True):
		try:
			method = raw_input('Which method among the three u want to try?\n(You can type in "quit" to quit the program.)\n'+"1.Top Agency Complaints for each Zipcode\n"+
				"2.Compare two agencies' complaints\n"+"3.Use circles to represent complaints number for each Zipcode\n"+'Type number 1, 2, or 3:\n')
			if method == 'quit' or method == 'q' or method =='Q' or method == 'Quit':
				sys.exit()
			if int(method) > 3:
				print ('\n!!Please select one of the numbers.(1, 2, or 3)\n')
			if int(method) == 1:
				mapPoints = getmapPoints(complaintsdata)
				k.TopAgencyforEachzipCode(mapPoints,dat)
				prompt()
			if int(method) == 2:
				m = getinput()
				agencymapPoints = getagencymapPoints(complaintsdata,m[0],m[1])
				k.comparetowagencies(agencymapPoints,dat)
				prompt()
			if int(method) ==3:
				zipmapPoints = getzipmapPoints(complaintsdata)
				k.plotzipcomplaints(zipmapPoints,dat)
				prompt()
			
		except ValueError:
			raise Exception ('There is a problem with the input you gave, please check it and run the program again.')
		