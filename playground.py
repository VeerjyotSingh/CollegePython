n = int(input("Please enter a number: "))
flag = 1

for i in range(2,n):
	if n%i == 0:
		flag = 0
		break

if flag == 0:
	print("not a prime")
else:
	print("A prime number")

#problem above code will give 0 and 1 also as prime number

