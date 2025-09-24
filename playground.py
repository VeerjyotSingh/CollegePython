class Numbers():
    def __init__(self,x,y):
        print("number is",x,"+",y,"i")
        self.x = x
        self.y = y
        
    def __add__(self,Number2):
        NewNumber = Numbers(self.x + Number2.x,self.y + Number2.y)
        return NewNumber
    
    def __mul__(self,Number2):
        NewNumber = Numbers(self.x * Number2.x,self.y * Number2.y)
        return NewNumber
    
n1 = Numbers(5,6)
n2 = Numbers(7,8)
n3 = n1 + n2
n4 = n1*n2

        