n1=input().lower()
n2=input().lower()
s1=''
s2=''
for i in n1:
    if i!=" ":
        s1+=i
for j in n2:
    if j!=" ":
        s2+=j
s=''
for k in s2:
    if k in s1 and k not in s:
        s+=k
a=(sorted(s))
if len(a)!=0:
    for i in a:
        print(i,end="")
else:
    print(-1)