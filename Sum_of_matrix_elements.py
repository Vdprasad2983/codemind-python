n=int(input())
m=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
l=0
for i in range(n):
    l+=sum(mat[i])
print(l)