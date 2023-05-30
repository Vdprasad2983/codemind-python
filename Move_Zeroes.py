n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i==0:
        b.append(i)
    else:
        a.append(i)
c=a+b
print(*c)