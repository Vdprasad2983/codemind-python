n=input().lower()
l=list(n.split())
a=l[0]
k=0
for i in range(len(a)):
    c=0
    for j in range(len(l)):
        if a[i] in l[j]:
            c+=1
    if c==len(l):
        print(a[i],end='')
        k+=1
if k==0:
    print(-1)