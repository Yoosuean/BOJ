#BOJ 1002 터렛
import math

t=int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dis=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))


    if dis==0 and r1==r2:
        print(-1)
    elif dis>r1+r2 or dis==0:
        print(0)
    elif dis ==r1+r2 or dis+min(r1,r2)==max(r1,r2):
        print(1)
    else: 
        print(2)

