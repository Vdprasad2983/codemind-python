n=input().lower()
a=n.split(" ")
d=[]
for i in a:
    for j in i:
        if n.count(j)==1:
            d.append(j)
for i in (sorted(d)):
    print(i,end="")