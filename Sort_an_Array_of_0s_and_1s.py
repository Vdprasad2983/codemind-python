n=int(input())
l=list(map(int,input().split()))
l.sort()
s = [str(integer) for integer in l]
a_string = " ".join(s)
res = str(a_string)
print(res)

