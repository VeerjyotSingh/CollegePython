"""Design a program that asks the user to enter a store’s sales for each day of the week. The
amounts should be stored in a list. Use a loop to calculate the total sales for the week and
display the result."""

def saleListMaker():
	saleList = []
	for i in range(7):
		salesInput = float(input("Please Enter the sales of "+str(i+1)+"day: "))
		saleList.append(salesInput)

	print("",saleList,sep="\n")
	print("Total Sales = ",sum(saleList))


if __name__ == "__main__":
	while True:
		print("","-"*20,sep="\n")
		print("Which Question do you want to do")
		x = int(input("Please enter the choice: "))
	
		if x == 1:
			saleListMaker()
	
		elif x == 2:
			#checking sort with mix datatype
			l = [49,29,39,12.34,123.213]
			l.sort()
			print("This will return an error only if the list contains a string")
			print(l)
		
		elif x == 3:
			l = [212,1,21,21,1,212,21]
			print("Before rm",l)
			l.remove(212)
			print("After rm",l)
		else:
			break
