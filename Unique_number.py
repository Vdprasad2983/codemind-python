n=int(input())
s=str(n)
for i in s:
    if s.count(i)!=1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")