s=input()
o=''
for i in s:
    if int(i)%2!=0:
        a=int(i)**2
        o+=str(a)
print(o)