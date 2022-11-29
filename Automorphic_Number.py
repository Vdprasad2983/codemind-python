n=int(input())
x=n**2
if x%10==n or x%100==n or x%1000==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")