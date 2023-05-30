n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        if l[i]>l[j]:
            s+=1
    a.append(s)
print(*a)