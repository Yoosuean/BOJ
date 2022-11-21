h,m=map(int,input().split())
cost=int(input())

m=m+cost
if m>59:
    h+=m//60
    m=m%60
    if h>23:
        h=h%23-1
print(h,m)