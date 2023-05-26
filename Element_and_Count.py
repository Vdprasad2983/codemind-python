a=int(input())
l=list(map(int,input().split()))
l1=[]
k=[]
for i in l:
    if i not in l1:
        l1.append(i)
for j in l1:
    k.append(j)
    k.append(l.count(j))
print(*k)    
    
    