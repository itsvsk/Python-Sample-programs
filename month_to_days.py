
ip=input("enter month name(without short form) :")
if ip in("January","March","May","July","August","October","December","january","march","may","july","august","october","december"):
    print(ip+" has 31 days");
elif ip in ("April","June","September","November","april","june","september","november"):
    print(ip+" has 30 days")
elif ip in("February","february") :
     print(ip+" can have 28 or 29 days")
else:
     print(ip+"is an invalid month")
