import math
a,b,c=map(int,input().split())
s=(1/2)*(a+b+c)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("%.2f"%area)