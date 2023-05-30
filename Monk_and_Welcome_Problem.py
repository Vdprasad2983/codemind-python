n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
for i in range(len(l1)):
    a.append(l1[i]+l2[i])
print(*a)