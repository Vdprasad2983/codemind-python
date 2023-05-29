n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
s=[]
for i in range(len(k)):
    if l.count(k[i])==1:
        s.append((k[i]))
if len(s)!=0:
    print(*s)
else:
    print(-1)