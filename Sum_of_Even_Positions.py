n=int(input())
lst=list(map(int,input().split()))
evens=[]
for i in range(n):
    if i%2==0:
        evens.append(lst[i])
print(sum(evens))