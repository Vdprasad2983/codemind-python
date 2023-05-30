n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
a=[]
for i in range(len(l1)):
    a.insert(l2[i],l1[i])
print(*a)