# Name: 	load_clean_data.py
# Author: 	Pan Ding
# Date: 	May 08, 2015
# Summary:	1) Defines a class to load the csv file to a dataframe and eliminates the irrelavant columns
# 			2) Defines a function that cleans the dataframe 
########################################################################################## 


import pandas as pd

class dataframe():
	'''load csv file and select relavant colomns'''

	def __init__(self):
		'''Instantiates a class object'''
		pass

	def load_csv(self):
		'''
		Loads a csv file
		Throws an exception when IOError occurs
		'''
		try:
			print "\nLoading data..."
			raw_df = pd.read_csv("../311_Service_Requests_from_2010_to_Present.csv", dtype = 'unicode')
		except IOError:
			print 'The file does not exit. Please check your file directory.'

		# Select relavent columns
		print "\nRemoving unrelavant columns..."
		self.df = raw_df[[u'Unique Key', u'Created Date', u'Agency', u'Agency Name', u'Incident Zip', u'Borough']]
		return self.df

def clean_df(df):
	"""
	Removes the rows with NAN values for Boroughs and Agencies
	and removes records unspecified in agency name
	"""
	df_clean = df.dropna(subset = ['Borough', 'Agency'])
	# Drop rows with Agency = 3-1-1
	df_clean = df_clean[df_clean['Agency']!='3-1-1']	
	return df_clean

			