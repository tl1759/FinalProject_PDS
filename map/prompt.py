import sys
def prompt():
	commitmessage = raw_input('Do you want to try another method? (y or n)')
	if commitmessage == 'y' or commitmessage == 'Y' or commitmessage =='Yes':
		pass 
	if commitmessage == 'n' or commitmessage =='N' or commitmessage =='No':
		print "Thanks,bye!"
		sys.exit() 
