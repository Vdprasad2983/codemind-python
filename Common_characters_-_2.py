n=input().lower()
l=list(n.split())
a=l[0]
k=[]
for i in range(len(a)):
    c=0
    for j in range(len(l)):
        if a[i] in l[j]:
            c+=1
    if c==len(l):
        k.append(a[i])
print(len(k))