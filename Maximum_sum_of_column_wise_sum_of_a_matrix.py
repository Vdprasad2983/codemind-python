n,m=map(int,input().split())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
m1=[]
for i in range(m):
    s=0
    for j in range(n):
        s+=mat[j][i]
    m1.append(s)
print(max(m1))