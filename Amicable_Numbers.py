a=int(input())
b=int(input())
c=[i for i in range(1,a) if a%i==0]
d=[i for i in range(1,b) if b%i==0]
if a==sum(d) and b==sum(c):
    print("Amicable")
else:
    print("Not Amicable")