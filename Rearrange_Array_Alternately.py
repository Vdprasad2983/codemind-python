t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    a=[]
    for i in range((len(l)//2)):
        a.append(s[-(i+1)])
        a.append(s[i])
    if n%2==0:
        print(*a)
    else:
        a.append(l[n//2])
        print(*a)