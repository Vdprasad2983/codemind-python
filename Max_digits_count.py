def count(n):
    s=str(n)
    c=0
    for j in s:
        if j.isdigit():
            c+=1
    return c
a=int(input())
s=0
l=list(map(int,input().split()))
x=count(max(l))
for i in l:
    if count(i)==x:
        s+=1
print(s)