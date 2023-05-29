n=int(input())
l=list(map(int,input().split()))
k=[l[i] for i in range(len(l)) if l.count(l[i])==1]
if len(k)!=0:
    print(max(k))
else:
    print(-1)