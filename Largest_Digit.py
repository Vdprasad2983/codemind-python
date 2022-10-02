n=int(input())
x=0
while n:
   d=n%10
   n=n//10
   if(d>x):
       x=d
print(x)