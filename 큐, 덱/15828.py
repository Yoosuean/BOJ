from collections import deque
import sys

n=int(sys.stdin.readline())
que=deque()

while True:
    packet=int(sys.stdin.readline())
    if packet==0:
        que.popleft()
    elif packet==-1:
        break;
    elif len(que)<n:
        que.append(packet)

if len(que)==0:
    print('empty')
else:
    for i in que:
        print(i)