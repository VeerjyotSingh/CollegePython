#Algorith Workbench

"""9.Assume list1 is a list of integers. Write a statement that uses a list comprehension to
create a second list containing the squares of the elements of list1."""

def listComprehension(list1):
    return [i**2 for i in list1]

"""Assume list1 is a list of integers. Write a statement that uses a list comprehension to
create a second list containing the elements of list1 that are greater than 100."""

def listComprehension2(list1):
    return [i for i in list1 if i >100]

"""Assume list1 is a list of integers. Write a statement that uses a list comprehension to
create a second list containing the elements of list1 that are even numbers."""

def listComprehension3(list1):
    return [i for i in list1 if i%2==0]

"""Write a statement that creates a two-dimensional list with 5 rows and 3 columns. Then
write nested loops that get an integer value from the user for each element in the list."""

def listComprehension4():
    m = int(input("Please enter a number of rows: "))
    n = int(input("Please enter a number of columns: "))
    twoDlist = []
    for i in range(m):
        row = []
        print(f"inputing row{i + 1}")
        for j in range(n):
            row.append(int(input("Please enter a number: ")))
        twoDlist.append(row)
    return twoDlist

while True:
    print("Which question do you want[1-4]")
    x = int(input("Please enter the question number: "))
    list1 = [1,2,3,4,5,5,6,7,9,9,32]
    print("Using list as",list1)
    if x == 1:
        print(listComprehension(list1))

    elif x == 2:
        print(listComprehension2(list1))

    elif x == 3:
        print(listComprehension3(list1))

    elif x == 4:
        print(listComprehension4())

    else:
        print("bye bye...")
        break