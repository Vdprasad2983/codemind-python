n=int(input())
s=n*n
l=len(str(n))
a=s%(10**l)
if n==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")