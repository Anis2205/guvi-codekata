while True:
	try:
		a=input()
		val=int(a)
		break
	except:
		print("the entered input is not a integer")
		break
if(val>0):
		print("Positive")
elif(val<0):
		print("Negative")
else:
		print("Zero")
