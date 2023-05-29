s1=input().lower()
s2=input().lower()
a=""
for i in s2:
    if i in s1 and i not in a and i!=" ":
        a+=i
k=sorted(a)
if len(k)!=0:
    for j in k:
        print(j,end="")
else:
    print(-1)