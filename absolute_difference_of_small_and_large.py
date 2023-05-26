n=list(input().split())
for i in n:
    x=ord(max(i))
    y=ord(min(i))
    print(abs(x-y),end=" ")