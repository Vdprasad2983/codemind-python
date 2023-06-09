n=int(input())
l=list(map(int,input().split()))
p=[i*i for i in range(1,100)]
s=0
for i in l:
    if i in p:
        s+=i
print(s)