ls = ['NA','','-343.34','no data','23423','-343']
for str in ls:
	try:
		print(float(str),'is a float')
	except ValueError:
		print('"'+str+'" is not a float')
