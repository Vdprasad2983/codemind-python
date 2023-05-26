n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    if i not in k:
        k.append(i)
for j in range(len(k)):
    if k[j]%2!=0:
        c+=1
print(c)