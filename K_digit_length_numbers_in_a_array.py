def count(n):
    s=str(n)
    c=0
    for j in s:
        if j.isdigit():
            c+=1
    return c
a,b=map(int,input().split())
s=0
l=list(map(int,input().split()))
for i in l:
    if count(i)==b:
        s+=1
print(s)