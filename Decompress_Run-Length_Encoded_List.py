n=int(input())
l=list(map(int,input().split()))
a=l[1::2]
b=l[::2]
x=[]
s=0
for i in b:
    for j in range(i):
        x.append(a[s])
    s+=1    
print(*x)