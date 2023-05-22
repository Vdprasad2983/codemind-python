n=int(input())
l=list(map(str,input().split()))
a=[]
a1=[]
for j in l:
    a.append(len(j))
for i in range(n):
    if a[i]==max(a):
        a1.append(l[i])
print(*a1)