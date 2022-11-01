n=int(input())
even=0
odd=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2==0:
        even+=l[i]
    else:
        odd+=l[i]
print(abs(even-odd))