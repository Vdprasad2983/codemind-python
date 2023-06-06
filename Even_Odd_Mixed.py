n=int(input())
s=str(n)
e=0
o=0
for i in s:
    if int(i)%2==0:
        e+=1
    else:
        o+=1
if len(s)==e:
    print("Even")
elif len(s)==o:
    print("Odd")
else:
    print("Mixed")