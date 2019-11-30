n1 =input("Input first number: ")
n2=input("Input second number: ")
n3=input("Input third number: ")
if n1 > n2:
    if n1 < n3:
        m= n1
    elif n2 > n3:
        m= n2
    else:
        m= n3
else:
    if n1 > n3:
        m= n1
    elif n2 < n3:
        m= n2
    else:
        m= n3

print("the median is", m)
