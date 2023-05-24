n=int(input())
l=list(map(int,input().split()))
first=l[:n//2]
second=l[n//2:]
x=(second[::-1]+first)
print(*x)