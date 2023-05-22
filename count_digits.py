def count(n):
    s=str(n)
    c=0
    for j in s:
        if j.isdigit():
            c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(count(i),end=" ")