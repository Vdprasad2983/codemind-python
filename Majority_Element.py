n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=[l.count(i) for i in s]
m=max(c)
for i in s:
    if l.count(i)==m:
        print(i)
        break