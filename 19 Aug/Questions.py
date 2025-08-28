from time import sleep

def Mod(x):
    if x < 0:
        return (x * (-1))
    else:
        return x

def divide(x, y):
    return x/y


while True:
    print("","-"*20,sep='\n')
    print("""1.Leap year
2.Voting Age
3.Even Odd
4.Grade
5.Last Digit
6.Sum of Digits
7.Divisible by 3
8.Divisible by 5
9.Mod of a Numbers
10.Divide
11.exit""")
    x = int(input("Enter your choice(Only Number): "))
    if x == 1:
        y = int(input("Enter year: "))
        if (y%4 == 0 and y%100 != 0) or y%400 == 0:
            print("leap year")
        else:
            print("Not a leap year")
    elif x == 2:
        y = int(input("Enter Age: "))
        if y >= 18:
            print("voting age")
        else:
            print("Not a voting age")
    elif x == 3:
        y = int(input("Enter a number: "))
        if y%2 == 0:
            print("even")
        else:
            print("odd")
    elif x == 4:
        y = int(input("Enter your score: "))
        if y >= 90:
            print("Your Grade is A")
        elif y >= 80:
            print("Your Grade is B")
        elif y >= 70:
            print("Your Grade is C")
        elif y >= 60:
            print("Your Grade is D")
        else:
            print("Your Grade is F")
    elif x == 5:
        y = int(input("Enter a number: "))
        lastDigit = y % 10
        print("Last digit is", lastDigit)
    elif x == 6:
        y = input("Enter a number: ")
        sum = 0
        for i in y:
            sum += int(i)
        print("Sum of digits is", sum)
    elif x == 7:
        y = int(input("Enter a number: "))
        if y%3 == 0:
            print("Divisble by 3")
        else:
            print("Not Divisble by 3")
    elif x == 8:
        y = int(input("Enter a number: "))
        if y%5 == 0:
            print("Divisble by 5")
        else:
            print("Not Divisble by 5")
    elif x == 9:
        y = int(input("Enter a number: "))
        print("Compliment is",Mod(y))
    elif x == 10:
        y = float(input("Enter a number: "))
        z = float(input("Enter a number: "))
        print(y,"/",z,"=",divide(y,z))
    else:
        break

    sleep(5)