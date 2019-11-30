class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b
x=float(input("\n enter length : "))
y=float(input("\n enter breadth : "))
ob=rect(x,y)
print("\n length",x," breadth ",y,". Area =",ob.area())
