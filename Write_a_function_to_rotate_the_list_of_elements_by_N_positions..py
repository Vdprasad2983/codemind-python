n=int(input())
l=list(map(int,input().split()))
k=int(input())
k=k%n
for i in range(n):
    if i<k:
        print(l[n+i-k],end=" ")
    else:
        print(l[i-k],end=" ")