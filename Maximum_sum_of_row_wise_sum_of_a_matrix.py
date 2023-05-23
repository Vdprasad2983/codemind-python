n,m=map(int,input().split())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
m1=[]
for i in range(n):
    s=0
    for j in range(m):
        s+=mat[i][j]
    m1.append(s)
print(max(m1))