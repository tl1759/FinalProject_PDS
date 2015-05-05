####################################################################################################
#
#
#	Author : Liwen Tian (tl1759)
#	DS GA 1007
#	Final Project
#
#	This module contains the class which will be used to plot the graphs
#
####################################################################################################


import math
from math import floor
from math import log
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers
from bokeh.objects import HoverTool
from collections import OrderedDict
import operator
class plotMaps():
	"""This is a class that plot the spatial analysis of 311 complaints data."""
	def __init__(self,zipBoroughdata):
		self.zipBoroughdata = zipBoroughdata

	def TopAgencyforEachzipCode(self,mapPoints,dat):
		"""This method is to create a choropleth map for NYC in which the shape color for each zipcode represents its 
		top agency in number of complaints."""
		
		plot = figure()
		polygons = {'lat_list':[],'lng_list':[],'color_list':[]} ##make a dict to 
		record_index = 0
		zipCodes = [];longitudes = [];latitudes = [];agencies_names = [];complaint_count = []
		colors = {'NYPD' : '#7f0000','DOT' : '#fee8c8','DEP' : '#fdd49e','DPR' : '#fdbb84','HPD' : '#fc8d59','FDNY' : '#ef6548','DOHMH' : '#d73000','TLC' : '#b30000'}
	
	
		for r in dat.iterRecords():
		
			currentZip = r[0]
		####make sure type of the data keep the same
			intzip = int(currentZip)

			if intzip in self.zipBoroughdata:
				zipCodes.append(intzip)				##get shape for this zip
				shape = dat.shapeRecord(record_index).shape
				points = shape.points
				lngs = [p[0] for p in points]
					
				lats = [p[1]for p in points]

				#store lat/lng for current zip shape
				polygons['lng_list'].append(lngs)
				polygons['lat_list'].append(lats)
				longitudes.append(lngs)
				latitudes.append(lats)
				##calculate color, according to number of complaints 
				if currentZip in mapPoints['zip_complaints']:
					sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(),key = operator.itemgetter(1),reverse = True)
					agency = sortedlist[0][0]
					complaints = sortedlist[0][1]
					##print zipcode,agency
					if agency in colors:
						agencies_names.append(agency)
						complaint_count.append(complaints)
						color = colors[agency]
					else:
						agencies_names.append('NA')
						complaint_count.append('NA')
						color = 'white'
				else:
					color = 'white'
					agencies_names.append('NA')
					complaint_count.append('NA')
				polygons['color_list'].append(color)
			record_index += 1
		file1 = output_file('TopAgencyForEachZipcode.html',title ="TopAgencyForZipCode ")
		TOOLS  = "pan,wheel_zoom,box_zoom,reset,hover,previewsave"
		source = ColumnDataSource(
			data = dict(
				longitudes = longitudes,
				latitudes = latitudes,
				agencies_names = agencies_names,
				complaint_count = complaint_count,
				zipCodes = zipCodes
				)
			)

		##create the polygons
		patches(polygons['lng_list'],polygons['lat_list'],\
			fill_color = polygons['color_list'],line_color = 'gray',\
			tools = TOOLS,plot_width = 1100, plot_height = 700,\
			title = 'Agency with top number of Complaints according to Zip Codes',source = source)
		hover = curplot().select(dict(type = HoverTool))
		hover.tooltips = OrderedDict([("Zip Code","@zipCodes"),("Top Agency Name","@agencies_names"),("Complaints","@complaint_count")])
		hold()
		x,y = -74.2,40.7
		for agency in colors:
			rect([x+0.01],[y],color = colors[agency],width = 0.01,height =.02)
			text([x],[y],text = agency,angle = 0,text_font_size = "8pt",font_weight = "bold",text_align = "right",text_baseline = "middle")
			y = y + .02
		show()

	

	def comparetowagencies(self,mapPoints,dat):
		"""This method is used to create an analogous map for NYC to compare two agencies in terms of number of complaints 
		for each zip code"""
		polygons = {'lat_list':[],'lng_list':[],'color_list':[]}# creates a dict for zip
		# color = ['#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b']
		color = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
		ratios = []
		trueratios = []
		ratio_colors = []
		agency_names = []
		zipCodes = []
		record_index = 0
		for r in dat.iterRecords():
			currentZip = r[0]
			intzip = int(currentZip)
			if intzip in self.zipBoroughdata:
				zipCodes.append(intzip)
				shape = dat.shapeRecord(record_index).shape
				points = shape.points
				lngs = [p[0] for p in points ]
				lats = [p[1] for p in points ]
				polygons['lng_list'].append(lngs)
				polygons['lat_list'].append(lats)
			####calculate ratio of number of complaints
				if currentZip in mapPoints['zip_complaints']:
					sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(),key = operator.itemgetter(0))
					if (sortedlist[0][1]+sortedlist[1][1]) == 0:
						ratios.append('NA')
					else:
						# trueratio = (float(sortedlist[0][1])/(sortedlist[0][1]+sortedlist[1][1]))*len(color)-1
						calculate_each_ratio = int(floor((float(sortedlist[0][1])/(sortedlist[0][1]+sortedlist[1][1]))*(len(color)-1)))
						ratios.append(calculate_each_ratio)
						# trueratios.append(trueratio)
					for i in ratios:
						if i=='NA':
							polygons['color_list'].append('white')
						else:
							ii = int(i)
							polygons['color_list'].append(color[ii])
			record_index += 1
		agency_names.append(sortedlist[1][0])
		agency_names.append(sortedlist[0][0])
		file2 = output_file("CompareTwoAgencies.html", title="ComapareTwoAgencies")
		TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave,hover"
		source = ColumnDataSource(
			data=dict(
			ratios = trueratios,
			zipCodes = zipCodes
				)
			)

	# Creates the polygons.
		patches(polygons['lng_list'], polygons['lat_list'], \
				fill_color=polygons['color_list'], line_color="gray", \
				tools=TOOLS, plot_width=1100, plot_height=700, \
				title="Ratio of Number of Complaints of selected agencies according to Zip Code",
				source = source)
		hover = curplot().select(dict(type=HoverTool))
		hover.tooltips = OrderedDict([("Zip Code", "@zipCodes")])
 
		
		hold()
		x, y1 = -74.2, 40.77
		y2 = 40.765

		for i, agency in enumerate(color):
			rect([x+0.01], [y1], color=color[i], width=0.01, height=.02)
			y1 = y1 + .01

			ratio_values = ['100% ', '100% ']

		for i, agency in enumerate(agency_names):
			text([x], [y2], text=ratio_values[i] + agency, angle=0, text_font_size="8pt", font_weight = 'bold', text_align="right", text_baseline="middle")
			y2 = y2 + 0.08

		show()

	def plotzipcomplaints(self,mapPoints,dat):
		"""This method is to draw a circle for each zipcode in NYC. The size of the circle is proportional to 
		the number of complaints in the zipcode"""
		
		numberOfComplaints = []
		polygons = polygons = {'lat_list':[],'lng_list':[],'radius_list':[]} 
		X = []
		Y = []
		zipCodes = []
		record_index = 0
		for r in dat.iterRecords():
			currentZip = r[0]
			intzip = int(currentZip)

		# Keeps only zip codes in NY area.
			if intzip in self.zipBoroughdata:
				zipCodes.append(intzip)
			# Gets shape for this zip.
				shape = dat.shapeRecord(record_index).shape
				points = shape.points

			# Breaks into lists for lat/lng.
				lngs = [p[0] for p in points]
				lats = [p[1] for p in points]

			# Stores lat/lng for current zip shape.
				polygons['lng_list'].append(lngs)
				polygons['lat_list'].append(lats)

				zip_box = shape.bbox
				lng_avg = (zip_box[0]+zip_box[2])/2
				lat_avg = (zip_box[1]+zip_box[3])/2

				X.append(lng_avg)
				Y.append(lat_avg)

			# Calculate ratio of number of complaints
				if currentZip in mapPoints['zip_complaints']:
					numberOfComplaints.append(mapPoints['zip_complaints'][currentZip])

			record_index += 1
		maxNumComplaints = max(numberOfComplaints)
		minNumComplaints = min(numberOfComplaints)
		sortedlist=[]

		for i in sorted(numberOfComplaints):
			sortedlist.append(i)

		for i in numberOfComplaints:
			polygons['radius_list'].append(i/(maxNumComplaints*float(100)))

	# # Creates the Plot
		File3 = output_file("plotZipComplaints.html", title="ZipComplaints")
		TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

	# Creates the polygons.
		patches(polygons['lng_list'], polygons['lat_list'], \
				fill_color = 'white', line_color="gray", \
				tools=TOOLS, plot_width=1100, plot_height=700, \
				title="Radius of circle according to the Number of Complaints in the Zip Code")
		hold()

		scatter(X,Y, fill_color='red',color='red', radius = polygons['radius_list'], alpha = 0.6, tools=TOOLS)

		show()


	