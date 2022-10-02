m,n=map(int,input().split())
for i in range(1,m*n+1):
    if(i%m==0 and i%n==0):
        print(i)
        break