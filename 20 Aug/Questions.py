# Print no. from -10 to -1

def printnumber():
    for i in range(-10,0):
        print(i)

def sumtill50():
    sum = 0
    for i in range(1,51):
        sum += i
    print("The sum is", sum)

def looptill5():
    for i in range(1,6):
        print(i)
    print("Loop has executed")

while True:
    print("-"*20)
    print("""Which one do you want to do?
    1.print number from -10 to -1
    2.print sum till 50
    3.print looptill 5 and print loop executed""")

    choice = int(input("Enter your choice[only the number]: "))
    if choice == 1:
        printnumber()
    elif choice == 2:
        sumtill50()
    elif choice == 3:
        looptill5()
    else:
        break

    print("")