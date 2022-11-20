from collections import deque
import sys

tc=int(input())

for _ in range(tc):
    count=0
    n,k=map(int,sys.stdin.readline().split())
    wait=deque(map(int,sys.stdin.readline().split()))
    while wait:
        max_num=max(wait)
        k-=1
        if max_num==wait[0]:
            count+=1
            if k<0:
                print(count)
                break;
            wait.popleft()
        else:
            wait.append(wait[0])
            wait.popleft()
            if k<0:
                k=len(wait)-1
            
            
                        
        
    

    