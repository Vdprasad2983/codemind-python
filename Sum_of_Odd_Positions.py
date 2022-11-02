n=int(input())
lst=list(map(int,input().split()))
odds=[]
for i in range(n):
    if i%2!=0:
        odds.append(lst[i])
print(sum(odds))