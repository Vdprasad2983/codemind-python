s=input()
s1=s.lower()
v=''
for i in s:
    if (not i.isdigit()) and (not i.isalpha()) and i!=" ":
        v+=i
print(len(v))