#Q1. Write a program to find the roots of a quadratic equation.
def rootsOfQuadratic():
	print("The following program requires you to input coefficient of varaibles")
	a = float(input("Enter the coefficient of x^2: "))
	b = float(input("Enter the coefficient of x: "))
	c = float(input("Enter the coefficient c: "))
	
	d = (b**2)-(4*a*c)
	if d < 0 :
		print("The following equations has no real roots")
		r1 = str(-(b/(2*a)))+" + "+str((abs(d)**0.5)/(2*a))+"i"
		r2 = str(-(b/(2*a)))+" - "+str((abs(d)**0.5)/(2*a))+"i"
		print("Roots are:- ")
		print("	",r1)
		print("	",r2)
	elif d >= 0 :
		print("The following equation has real roots")
		r1 = (-b+((d)**0.5))/(2*a)
		r2 = (-b-((d)**0.5))/(2*a)
		print("Roots are:- ")
		print("	",r1)
		print("	",r2)

"""2. Write a program to accept a number ‘n’ and
	a. Check if ’n’ is prime
	b. Generate all prime numbers till ‘n’
	c. Generate first ‘n’ prime numbers
	This program may be done using functions."""

def isPrime(n,primeList = []):
	if n <= 1:
		return False
	elif n == 2:
		return True
	elif n%2 == 0:
		return False
	else:
		if primeList:
			for p in primeList:
				if p * p > n:
					break
				if n % p == 0:
					return False
			return True
		else:
			for i in range(3,((int(n**0.5))+1),2):
				if n%i == 0:
					return False

		return True

def allPrimeTill(n):
	primeList = []
	for i in range(2,n+1):
		if isPrime(i,primeList):
			primeList.append(i)
	return primeList

def firstnPrimeNumbers(n):
	primeList = []
	m = 2	
	while True:
		if isPrime(m,primeList):
			primeList.append(m)
		if len(primeList) == n:
			break
		m+=1
	return primeList

#3.Writa a program to create a pyramid of the character ‘*’ and a reverse pyramid

def pyramid(n,reverse = False):
	if not reverse:
		for i in range(1,n+1):
			print(" "*(n-i),"*"*((2*i)-1))		
	else:
		for i in range(n,0,-1):
			print(" "*(n-i),"*"*((2*i)-1))

"""4. Write a program that accepts a character and performs the following:
	a. print whether the character is a letter or numeric digit or a special character.
	b. if the character is a letter, print whether the letter is uppercase or lowercase
	c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)"""

def check(chr):
	if len(chr) == 1:
		if chr.isdigit():
			print("The character provided is a Digit")
			numberNames = ["zero","one","two","three","four","five","six","seven","eight","nine"]
			print("Number name is,",numberNames[int(chr)])
		elif chr.isalpha():
			print("The character provided is an alphabet")
			if chr.isupper():
				print("The character is uppercase")
			else:
				print("The character is lowecase")
		else:
			print("The character provided is a special character")
	else:
		print("please provide only one character")

"""5.Write a program to perform the following operations on a string
	a. Find the frequency of a character in a string.
	b. Replace a character by another character in a string.
	c. Remove the first occurrence of a character from a string.
	d. Remove all occurrences of a character from a string."""

if __name__ == "__main__":
	while True:
		print("","-"*30,"",sep="\n")
		print("Which question do you want:[1-5] ")
		x = int(input("Please enter your choice: "))
		if x == 1:
			rootsOfQuadratic()
	
		elif x == 2:
			n = int(input("Enter the number: "))
			if isPrime(n):
				print(f"{n} is a prime number")
			else:
				print(f"{n} is not a prime number")

			print(f"All prime number till {n} are {allPrimeTill(n)}")
			print(f"First {n} prime numebers are {firstnPrimeNumbers(n)}")
		
		elif x == 3:
			n = int(input("How many lines do you want your pyramid: "))
			rev = input("Do you want reverse pyramid [t/f]: ")
			if rev.lower() == "t":
				rev = True
			else:
				rev = False
			pyramid(n,rev)
		
		elif x == 4:
			chr = input("Enter the character: ")
			check(chr)
		
		elif x == 5:
			str = input("Please enter the main string: ")
			sub = input("Please enter the sub string: ")
			chr = input("Please enter the character you want to replace sub with: ")
			print(f"Frequency of {sub} in {str} is {str.count(sub)}")
			print(f"{str} without first {sub} is {str.replace(sub, '',1 )}")
			print(f"{str} without {sub} is {str.replace(sub,'')}")
			print(f"{str} with {sub} as {chr} is {str.replace(sub,chr)}")
			
		else:
			print("bye bye..")
			break
