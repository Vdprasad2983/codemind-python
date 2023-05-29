def length(n):
    s=str(n)
    return len(s)
n=int(input())
l=list(map(int,input().split()))
l1=[length(i) for i in l if length(i)%2==0]
print(len(l1))