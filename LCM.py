a,b=map(int,input().split())
m1=[a*i for i in range(1,100)]
m2=[b*i for i in range(1,100)]
c=[i for i in m1 if i in m2]
print(c[0])