n=input().lower()
a=n.split(" ")
d=[]
for i in a:
    for j in i:
        if n.count(j)==1:
            d.append(j)
if len(d)!=0:
    print(d[0])
else:
    print(-1)