"""11. Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following operations:
	a. Print half the values of the tuple in one line and the other half in the next line.
	b. Print another tuple whose values are even numbers in the given tuple.
	c. Concatenate a tuple t2=(11,13,15) with t1.
	d. Return maximum and minimum value from this tuple"""

def printHalfTuple(t1):
	length = len(t1)
	if length%2 != 0 :
		length +=1 #this will allow us to split tuple with odd number of elements
	print("First Half of tuple",t1[:int(length/2)])
	print("Second Half of tuple",t1[int(length/2):])

def tupleWithEvenNumbers(t):
	l = []
	for i in t:
		try: 
			i = int(i)
			if i%2 == 0:
				l.append(i)
		except:
			continue
	return tuple(l)

def minMaxTuple(t):
	l = []
	for i in t:
		try:
			i = int(i)
			l.append(i)
		except:
			continue
	return min(l),max(l)
	

if __name__ == "__main__":
	while True:
		print("","-"*30,"",sep = "\n")
		print("Which Question do you want solution to?")
		try:
			x = int(input("Please enter your choice[11-15]: "))
		except:
			print("Please only input a number")
			continue
		
		if x == 11:
			t = input("Please input a tuple: ")
			t = t.strip("(")
			t = t.strip(")")	
			
			if t:
				t = tuple(t.split(","))
			else:
				t = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
			
			printHalfTuple(t)
			print("Tuple of only even numbers is",tupleWithEvenNumbers(t))
			
			t += (11,13,15)
			print("Concatinated Tuple is",t)
			min, max = minMaxTuple(t)
			print("Minimum value from the tuple is",min)
			print("Maximum value from the tuple is",max)
		else:
			print("bye bye.")
			break
