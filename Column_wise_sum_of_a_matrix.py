n,m=map(int,input().split())
mat=[]
for k in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(m):
    s=0
    for j in range(n):
        s+=mat[j][i]
    print(s,end=" ")