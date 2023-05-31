def rev(n):
    s=str(n)
    return int(s[::-1])
n=int(input())
s=n**2
r=rev(n)
s_r=r**2
if s==rev(s_r):
    print(True)
else:
    print(False)