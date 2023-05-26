n=int(input())
m1=[list(map(int,input().split())) for i in range(n)]
m2=[list(map(int,input().split())) for i in range(n)]
a=[]
for i in range(n):
    s=[]
    for j in range(n):
        x=abs(m1[i][j]-m2[i][j])
        s.append(x)
    a.append(s)
for i in a:
    print(*i)