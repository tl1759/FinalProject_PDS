####################################################################################################
#
#
#	Author : Liwen Tian(tl1759)
#	DS GA 1007
#	Final Project
#
#	This is the users input module.
#
####################################################################################################
import csv
import shapefile
import pandas as pd
import numpy as np
from cleanupModule import *
from plotModule import *
import sys
agencyList = ['HPD','DOT','NYPD','FDNY','DEP','DOHMH','DPR','TLC']
def getinput():

	print "Choose two different agencies in the agencies' List:"
	print agencyList


	agency1 = raw_input('Please choose the first agency:\n')
	agency2 = raw_input('please choose the second agency:\n')
	if agency1 in agencyList and agency2 in agencyList:
		pass
		
	else:
		print "Error: Agencies are not correctly selected!"
		print "Please make sure the agency is in the list otherwise the output is not valid.\n"+" There are no such agencies. ("+agency1+','+agency2+")"
		sys.exit()

	return agency1,agency2


		

