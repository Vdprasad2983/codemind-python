def sum_of_digits(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s=s+d
    return s
def product_of_digits(n):
    p=1
    while n:
        d=n%10
        n=n//10
        p=p*d
    return p
n=int(input())
s=sum_of_digits(n)
p=product_of_digits(n)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")