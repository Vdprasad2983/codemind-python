n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=[l.count(i) for i in s]
s1=0
for j in range(len(l1)):
    if l1[j]>=2:
        s1+=int(l1[j])//2
print(s1)