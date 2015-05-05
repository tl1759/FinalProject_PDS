####################################################################################################
#
#
#	Author : Liwen Tian (tl1759)
#	DS GA 1007
#	Final Project
#
#	This is the module that contains different methods of cleaning data.
####################################################################################################



def getzipBorough(zipdata):
	""""this is the method to get zipdata"""
	zipBorough = {}
	for i in range(len(zipdata)):
			zipBorough[zipdata['Incident Zip'][i]]= zipdata['Borough'][i]
	return zipBorough
def getmapPoints(complaintsdata):
	"""get mapPoints for top agency for each zipCode"""
	agencyDict = {};complaintsPerZip = {};mapPoints = {};lat = [];lng = []
	for i in range(len(complaintsdata)):
			try:
				lat.append(float(complaintsdata['Latitude'][i]))
				lng.append(float(complaintsdata['Longitude'][i]))
				agency = complaintsdata['Agency'][i] #list of agnecies
				zipCode = complaintsdata['Incident Zip'][i]#list of zipcodes
				if not agency in agencyDict:
					agencyDict[agency] = len(agencyDict)## agency as key and values is the leghth of the dictionary
				if zipCode in complaintsPerZip:##zipcode as a key 
					if agency in complaintsPerZip[zipCode]: ## value is also a dictionary{agency:number}
						complaintsPerZip[zipCode][agency] += 1
					else:
						complaintsPerZip[zipCode][agency] = 1

				else:
					complaintsPerZip[zipCode] = {}
					complaintsPerZip[zipCode][agency] = 1

			except:
				pass
	mapPoints = {'zip_complaints':complaintsPerZip}
	return mapPoints
def getagencymapPoints(data,agency1,agency2):
	"""get two agenies mapPoints"""
	complaintsPerZip = {};lat = [];lng = [];
	for i in range(len(data)):
		try:
			lat.append(float(data['Latitude'][i]))
			lng.append(float(data['Longitude'][i]))
			agency = data['Agency'][i] #list of agnecies
			zipCode = data['Incident Zip'][i]
			if zipCode in complaintsPerZip:
				if agency == agency1:
					if agency in complaintsPerZip[zipCode]:
						complaintsPerZip[zipCode][agency]+=1
					else:
						complaintsPerZip[zipCode][agency] = 1
				elif agency == agency2:
					if agency in complaintsPerZip[zipCode]:
						complaintsPerZip[zipCode][agency]+=1
					else:
						complaintsPerZip[zipCode][agency] = 1
				else:
					pass
			else:
				complaintsPerZip[zipCode]={agency1:0,agency2:0}
		except:
			pass
	agencymapPoints = {'zip_complaints':complaintsPerZip}
	return agencymapPoints

def getzipmapPoints(complaintsdata):
	"this is the method that get number of complaints  for each zipcodes"
	complaintsPerZip = {}
	lat = []
	lng = []
	for i in range(len(complaintsdata)):
		try:
			lat.append(float(complaintsdata['Latitude'][i]))
			lng.append(float(complaintsdata['Longitude'][i]))
			agency = complaintsdata['Agency'][i] #list of agnecies
			zipCode = complaintsdata['Incident Zip'][i]#list of zipcodes
			if zipCode in complaintsPerZip:
				complaintsPerZip[zipCode]+=1
			else:
				complaintsPerZip[zipCode]=1

		except:
			pass
	zipmapPoints = {'zip_complaints':complaintsPerZip}
	return zipmapPoints