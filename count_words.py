n=input()
s=n.lower()
l=list(s.split(" "))
c=0
for i in l:
    if i[0] in "aeiou" and i[-1] not in "aeiou":
        c+=1
print(c)