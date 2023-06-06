n1=input().lower()
n2=input().lower()
s1=n1.split()
s2=n2.split()
l=[]
for i in s2:
    if i in s1:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(*l)