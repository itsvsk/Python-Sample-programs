print("enter sides of triangle :")
a=input("side 1 :")
b=input("side 2 :")
c=input("side 3 :")
if a==b==c:
    print("Euilateral traingle")
elif a==b or a==c or b==c :
    print("isoceles triangle")
else:
    print("scalene triangle")
