while True:
	try:
		a=input()
		val=int(a)
		break
	except:
		print("invalid")
		break
if(val<0):
	print("invalid")
elif(val%2==0):
    print("even")
else:
	print("odd")
