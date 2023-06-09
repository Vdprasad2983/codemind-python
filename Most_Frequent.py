n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
c=[l.count(i) for i in s]
m=c.index(max(c))
print(s[m])