def NextTime(time):
	h,m = time.split(':')
	minutes = int(h)*60 + int(m) # Convert hours into minutes 
	for i in range(minutes+1, minutes+1441): # We start iteratingn from the next minute upto 24 hours added
		t= i%1440 # Modulo makes sure we do not get 24, 25.. values 
		h, m = t//60, t%60 # converting minutes back 
		res= "{:02d}:{:02d}".format(h,m) #Formatting back to time format 
		if set(res) <= set(time): #Direct comparison 
			break
	return res


print(NextTime("10:59"))

