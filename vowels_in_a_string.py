n=input()
l=list(n)
m=input()
if m in l:
    print(True)
    print(l.index(m))
else:
    print(False)