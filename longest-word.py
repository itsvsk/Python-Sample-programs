txt=input("enter list of words :")

l=0

for wrd in txt.split():
    if len(wrd)>l:
        l=len(wrd)
        lwrd=wrd
print("longest word : "+lwrd+" ,length = "+str(len(lwrd)))

