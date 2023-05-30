n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    p=1
    for j in range(len(l)):
        if i==j:
            continue
        else:
            p*=l[j]
    l1.append(p)
print(*l1)