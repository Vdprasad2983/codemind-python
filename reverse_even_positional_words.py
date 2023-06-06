n=input().split()
for i in range(0,len(n),2):
    n[i]=n[i][::-1]
print(*n)