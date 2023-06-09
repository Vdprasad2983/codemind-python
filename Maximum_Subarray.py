n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(i+1,n+1):
        a.append(sum(l[i:j]))
print(max(a))