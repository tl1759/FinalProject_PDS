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
from cleanupModule import *
from plotmapModule import *
from userinput import *
from prompt import *
if __name__ == '__main__':
	print "Now it's loading the data and it may take some time, thank you for your patience!"
	try:
	#Read in the complaintsdata 
		complaintsdata = pd.read_csv(sys.argv[1],low_memory = False)
		zipcodedata = pd.read_csv(sys.argv[2]) #load zipcode data with pandas
		dat = shapefile.Reader(sys.argv[3])# load shapefile
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
				"2.Compare two agencies' complaints\n"+"3.Use circles to represent complaints number for each Zipcode\n"+'Type number 1, 2, 3 or just quit the program:\n')
			if method == 'quit' or method == 'q' or method =='Q' or method == 'Quit':
				print "You just quit the program. Thanks, bye!"
				sys.exit()
			# elif int(method) > 3:
			# 	print ('\n!!Please select one of the numbers.(1, 2, or 3)\n')
			elif int(method) == 1:
				print "You have choose method 1. It is drawing map now, and it may take a while, thank you for your patience."
				mapPoints = getmapPoints(complaintsdata)
				k.TopAgencyforEachzipCode(mapPoints,dat)
				prompt()
			elif int(method) == 2:
				print "You have choose method 2. It is drawing map now, and it may take a while, thank you for your patience."
				m = getinput()
				agencymapPoints = getagencymapPoints(complaintsdata,m[0],m[1])
				k.comparetowagencies(agencymapPoints,dat)
				prompt()
			elif int(method) ==3:
				print "You have choose method 3. It is drawing map now, and it may take a while, thank you for your patience."
				zipmapPoints = getzipmapPoints(complaintsdata)
				k.plotzipcomplaints(zipmapPoints,dat)
				prompt()
			else:
				print "\n Make sure your are selecting method's number!\n"
			
		except ValueError:
			raise Exception ('There is a ValueError with the input you gave, please check it and run the program again.')
		