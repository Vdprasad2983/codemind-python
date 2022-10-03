a=int(input())
b=int(input())
s1=0
for i in range(1,a):
    if a%i==0:
        s1=s1+i
s2=0
for i in range(1,b):
    if b%i==0:
        s2=s2+i
if(a==s2 and b==s1):
    print("Amicable")
else:
    print("Not Amicable")
