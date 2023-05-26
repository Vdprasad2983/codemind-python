n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[i for i in l if a>i or b<i]
if k==[]:
    print(-1)
else:
    print(max(k))