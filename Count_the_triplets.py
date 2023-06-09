t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]+l[j] in l:
                a=a+1
    if a==0:
        print("-1")
    else:
        print(a)
            