n=input()
s=''
for i in n:
    if i in "aeiou" and i not in s:
        s+=i
s1=''
for i in n:
    if i in "AEIOU" and i not in s1:
        s1+=i
if len(s)==5 or len(s1)==5:
    print(True)
else:
    print(False)