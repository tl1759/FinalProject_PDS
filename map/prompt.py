import sys
def prompt():
	i = True
	while  (i == True):

		commitmessage = raw_input('Do you want to try another method? (y or n)')
		if commitmessage == 'y' or commitmessage == 'Y' or commitmessage =='Yes':
			i = False
			pass
		elif commitmessage == 'n' or commitmessage =='N' or commitmessage =='No':
			print "Thanks,bye!"
			sys.exit() 
		else:
			print "Please type in N OR Y to go on with the program."

