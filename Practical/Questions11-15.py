from sys import exit

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
	
"""12. Define a class Employee that stores information about employees in the company. The class should contain the following:
	(i) data members- count (to keep a record of all the objects being created for this class) and for every employee: an employee number, Name, Dept, Basic, DA and HRA.
	(ii) function members:
		a. __init__ method to initialize and/or update the members. Add statements to ensure that the program is terminated if any of Basic, DA and HRA is set to a negative value.
		b. function salary, that returns salary as the sum of Basic, DA and HRA.
		c. __del__ function to decrease the number of objects created for the class.
		d. __str __ function to display the details of an employee along with the salary of an employee in a proper format."""

class Employee():
	count = 0 #this will keep a record of number of objects being created
	def __init__(self,empNum,name,dept,basic,da,hra):
		if basic < 0 or da < 0 or hra < 0:
			exit(1) #exit with code 1 (which means some error has occured)
		print(f"A new Employee object named {empNum} is being created")
		self.empNum = empNum
		self.name = name
		self.dept = dept
		self.basic = basic
		self.da = da
		self.hra  = hra
		
		Employee.count += 1 #updating count variable to reflect creation of new object
	
	def __del__(self):
		Employee.count -=1
		print("The employee has been layed off")

	def __str__(self):
		return (
            		f"\nEmployee No : {self.empNum}\n"
            		f"Name        : {self.name}\n"
            		f"Department  : {self.dept}\n"
            		f"Basic       : {self.basic}\n"
            		f"DA          : {self.da}\n"
            		f"HRA         : {self.hra}\n"
            		f"Total Salary: {self.salary()}"
        )	

	def salary(self):
		return self.basic + self.da + self.hra


#13. Write a program to define a class "2DPoint" with coordinates x and y as attributes. Create relevant methods and print the objects. Also define a method distance to calculate the distance between any two point objects.

class TwoDPoint:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return (f"Coordinates are ({self.x},{self.y})")
	
	def distance(self,Point2):
		return ((Point2.x - self.x)**2 + (Point2.y - self.y)**2)**0.5


#14. Inherit the above class to create a "3Dpoint" with additional attribute z. Override the method defined in "2DPoint" class , to calculate distance between two points of the "3DPoint" class.

class ThreeDPoint(TwoDPoint):
	def __init__(self,x,y,z):
		super().__init__(x,y)
		self.z = z
	
	def __str__(self):
		return (f"Coordinates are ({self.x},{self.y},{self.z})")

	def distance(self,Point2):
                return ((Point2.x - self.x)**2 + (Point2.y - self.y)**2 + (Point2.z - self.z)**2)**0.5
		

#15. Write a program to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters.

def askForName():
	# will ask the user to enter name again untill correct name is not entered
	name = ""
	while True:
		name = input("Please input a valid name: ")
		if name.isalpha():
			break
		else:
			print("please input a name without any special characters or digits")
	return name
	

if __name__ == "__main__":
	empList = []
	twoDPointList = [TwoDPoint(0,0)]
	threeDPointList = [ThreeDPoint(0,0,0)]

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
	
		elif x == 12:
			empNum = int(input("Please enter the employee Number: "))
			name = input("Please enter the employee name: ")
			dept = input("Please input the department: ")
			basic = float(input("Please input the basic salary: "))
			da = float(input("Please input the DA: "))
			hra  = float(input("Please input the HRA: "))
			emp = Employee(empNum,name,dept,basic,da,hra)
			empList.append(emp)
			print(emp)
		
		elif x == 13:
			x = float(input("Enter the x coordinate: "))
			y = float(input("Enter the y coordinate: "))
			point = TwoDPoint(x,y)
			print(point)
			twoDPointList.append(point)			
			print("Distance from Origin is",point.distance(twoDPointList[0]))
		
		elif x == 14:
			x = float(input("Enter the x coordinate: "))
			y = float(input("Enter the y coordinate: "))
			z = float(input("Enter the z coordinate: "))
			point = ThreeDPoint(x,y,z)
			print(point)
			threeDPointList.append(point)
			print("Distance from Origin is",point.distance(threeDPointList[0]))
		
		elif x == 15:
			name = askForName()
			print(f"Your name is {name}")
		
		else:
			print("bye bye.")
			break



