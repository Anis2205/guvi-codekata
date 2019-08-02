a=int(input())
if(a%4==0):
	if(a%100==0):
		if(a%400==0):
			print("yes")
		else:
			print("no")
	else:
		print("yes")
else:
	print("no")
	
