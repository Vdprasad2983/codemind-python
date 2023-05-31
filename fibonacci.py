n=int(input())
l=[]
l.append(0)
l.append(1)
for i in range(2,n):
    l.append(l[i-1]+l[i-2])
print(*l)