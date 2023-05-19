n=input()
x=n.lower()
lst=list(set(x))
c=0
for i in lst:
    if i==" ":
        continue
    else:
        c+=1
print(c)