n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if l.count(i)==i and i not in k:
        k.append(i)
print(len(k))