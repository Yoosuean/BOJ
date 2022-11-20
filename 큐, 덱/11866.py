from collections import deque

n,k=map(int,input().split())

dq=deque(range(1,n+1))
res=list()

while len(dq)>0:
    for _ in range(k-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())


print("<",end='')
for i in range(len(res)-1):
    print(res[i],end=', ')
print(res[-1],end='')
print(">")
