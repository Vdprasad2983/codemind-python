n,m=map(int,input().split())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
l=[]
for i in range(len(mat)):
    l.append(sum(mat[i]))
print(max(l))