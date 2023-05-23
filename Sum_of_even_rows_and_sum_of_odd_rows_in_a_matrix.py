n,m=map(int,input().split())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
e=0
o=0
for j in range(len(mat)):
    if j%2==0:
        e+=sum(mat[j])
    else:
        o+=sum(mat[j])
print(e,o)