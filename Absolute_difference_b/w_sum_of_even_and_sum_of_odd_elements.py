n=int(input())
lst=list(map(int,input().split()))
even=[lst[i] for i in range(n) if lst[i]%2==0]
odd=[lst[i] for i in range(n) if lst[i]%2!=0]
print(abs(sum(even)-sum(odd)))