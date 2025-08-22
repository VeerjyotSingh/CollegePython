from math import pi


def add_number(num1,num2):
    return num1+num2

def Area_Circle(radius):
    return radius*radius*pi

def Celcius_to_Fahrenheit(Celsius):
    return (Celsius*9/5) + 32

def Perimeter_Rectangle(width, height):
    return (width+height)*2

def Cube_Number(x):
    return x**3

def Basic_Maths(a,b):
    return (a+b,a-b,a*b,a/b)

def sphere_Measurment(Radius):
    return ((Radius**3)*pi*3/4,4*pi*(Radius**2))

def Calculate_Simple_Interest(p,r,t):
    return p*r*t/100

def repeat_words(word,n):
    return word*n

def Full_Name(First,Last):
    return First+" "+Last


while True:
    print("-"*20)
    print("Which function do you want to use?")
    print("""        1.Add Number
        2.Area Circle
        3.Celcius to Fahrenheit
        4.Perimeter Rectangle
        5.Cube Number
        6.Basic Maths
        7.Sphere Measurment
        8.Simple Interest
        9.Repeat Words
        10.Full Name
        11.Quite""")

    choice = int(input("Enter your choice: "))
    ans = ""
    if choice == 1:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        ans = add_number(x,y)
    elif choice == 2:
        r = float(input("Enter radius: "))
        ans = Area_Circle(r)
    elif choice == 3:
        f = float(input("Enter Temperature: "))
        ans = Celcius_to_Fahrenheit(f)
    elif choice == 4:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        ans = Perimeter_Rectangle(x,y)
    elif choice == 5:
        x = float(input("Enter first number: "))
        ans = Cube_Number(x)
    elif choice == 6:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        ans = Basic_Maths(x,y)
    elif choice == 7:
        x = float(input("Enter radius: "))
        ans = sphere_Measurment(x)
    elif choice == 8:
        p = float(input("Enter Principle: "))
        r = float(input("Enter rate: "))
        t = float(input("Enter time: "))
        ans = Calculate_Simple_Interest(p,r,t)
    elif choice == 9:
        word = input("Enter word: ")
        n = int(input("Enter number of iterations: "))
        ans = repeat_words(word,n)
    elif choice == 10:
        x = input("Enter first name: ")
        y = input("Enter second name: ")
        ans = Full_Name(x,y)
    else:
        break

    print(ans)
