n=int(input())
weight=[int(input()) for i in range(n)]
t=int(input())
total=0
for i in weight:
    if i<=t:
        total+=1
    else:
        total+=2
print(total)