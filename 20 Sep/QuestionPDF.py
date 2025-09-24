productList = [["Laptop",800],["Smartphone",500],["Tablet",300]]

#Here we are creating a shallow copy which implies that a seperate new list is being created
#i.e. variables copyProducts and productList don't share same memory location
#A deep copy is where both variables point to the same underlying memory thus changes made to one will reflect to the other
copyProducts = productList.copy()
copyProducts[1][1] = 550
copyProducts[2] = ['Smartwatch', 250]

print(productList)
print(copyProducts)

def printPattern(n):
    for i in range(1,n+2):
        for x in range(1,i):
            print(x,end="")
        print()

printPattern(5)

def squareEvenPos(inList):
    return [i**2 for i in inList if i%2 == 0 and i>0]

print(squareEvenPos([1,2,3,4,5,-1,-2]))

players = "kohli and rohit play great game"
print(players.rfind ('i'))
players = players.swapcase()
players = players.lstrip()
print(players.endswith('!!'))
players = players.replace('GREAT', 'outstanding')

print(players)


