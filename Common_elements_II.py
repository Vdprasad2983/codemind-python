a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
s3=s1.intersection(s2)
l3=list(s3)
c=[]
for i in l1:
    if i not in l3:
        c.append(i)
for j in l2:
    if j not in l3:
        c.append(j)
print(*c)