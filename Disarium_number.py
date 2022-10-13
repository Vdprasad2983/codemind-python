n=int(input())
c=len(str(n))
temp=n
sum=0
while n!=0:
    d=n%10
    n=n//10
    sum+=d**c
    c-=1
if sum==temp:
    print(True)
else:
    print(False)