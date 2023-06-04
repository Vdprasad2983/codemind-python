n=int(input())
l=[]
for i in range(1,n+1):
    l.append((chr(64+i)+" ")*i)
l_l=l[::-1]
for j in l_l:
    print(j)