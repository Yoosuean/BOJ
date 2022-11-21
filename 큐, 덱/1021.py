from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
wait = list(map(int,sys.stdin.readline().split())) 
dq=deque(range(1,n+1))
count=0



for i in wait:
    while dq:
        if dq[0]==i:
            dq.popleft()
            break
        else:
            if dq.index(i)<len(dq)/2:
                while dq[0]!=i:
                    dq.append(dq.popleft())
                    count+=1
            else:
                while dq[0]!=i:
                    dq.appendleft(dq.pop())
                    count+=1
print(count)