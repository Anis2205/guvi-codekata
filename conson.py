ch=input()
if((ch>="a" and ch<="z") or (ch>="A" and ch<="z")):
	if(ch==("a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U")):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
