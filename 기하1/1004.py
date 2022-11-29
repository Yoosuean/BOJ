import sys
import math

t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    count=0
    n=int(sys.stdin.readline())
    for _ in range(n):
        c1,c2,r=map(int,sys.stdin.readline().split())
        start=math.sqrt(math.pow(x1-c1,2)+math.pow(y1-c2,2))
        end=math.sqrt(math.pow(c1-x2,2)+math.pow(c2-y2,2))
        
        if start<r and end<r:
            pass
        elif start<r or end<r:
            count+=1
    print(count)