a=input()
x='aeiou'
l=[]
for i in a:
    if i not in l and i in x:
        l.append(i)
if len(l)==5:
   print(0)
else:
    for j in x:
        if j not in l:
            print(j,end=" ")