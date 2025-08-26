def firstPattern(n):
	for i in range(1,n+1):
		print("*"*i)

def secondPattern(n):
	for i in range(1,n+1):
		print(" "*(n-i),"*"*i)

def thirdPattern(n):
	for i in range(1,n+1):
		for x in range(1,i+1):
			print(x,end=" ")
		print("")

def fourthPattern(n):
	x = 65
	for i in range(1,n+1):
		for i in range(i):
			print(chr(x+i),end="")
		print("")

def fifthPattern(n):
	x = 65
	for i in range(1,n+1):
		for i in range(i):
			print(chr(x),end="")
			x += 1
		print("")

def sixthPattern(n):
	for i in range(1,n+1):
		print(str(i)*n)

def seventhPattern(n):
	for i in range(n,0,-1):
		print("*"*i)


while True:
	m = int(input("Enter the pattern number you want: "))
	n = int(input("Enter the Number: "))
	if m == 1:
		firstPattern(n)
	elif m == 2:
		secondPattern(n)
	elif m == 3:
		thirdPattern(n)
	elif m == 4:
		fourthPattern(n)
	elif m == 5:
		fifthPattern(n)
	elif m == 6:
		sixthPattern(n)
	elif m == 7:
		seventhPattern(n)
	else:
		print("Bye Bye...")
		break
