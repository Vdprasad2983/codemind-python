n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
a=0
s=[]
for i in l:
    if i==k:
        s.append(a)
        c+=1
    a+=1
if len(s)!=0:
    print(s[0],s[-1])
else:
    print(-1,-1)