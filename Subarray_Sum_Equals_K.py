n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(i+1,n+1):
        a.append(sum(l[i:j]))
c=0
for i in a:
    if i==k:
        c+=1
print(c)
        