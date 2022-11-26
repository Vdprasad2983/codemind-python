n=int(input())
lst=list(map(int,input().split()))
a=(sum(lst)//n)
x=[i for i in lst if i<=a]
print(len(x))