t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    k=k%n
    a=[]
    for i in range(n):
        if i<k:
            a.append(l[n+i-k])
        else:
            a.append(l[i-k])
    print(*a)