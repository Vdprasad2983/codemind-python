n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
temp=[]
s=0
for i in range(n):
    for j in range(m):
        if (i==j or i+j==len(mat)-1) and [i,j] not in temp:
            temp.append([i,j])
            s+=mat[i][j]
print(s)