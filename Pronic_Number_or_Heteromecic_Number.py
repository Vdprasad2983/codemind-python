n=int(input())
p=[(i*(i-1)) for i in range(1,n)]
if n in p:
    print("YES")
else:
    print("NO")