from collections import deque

tc=int(input())

for _ in range(tc):
    command=list(input())
    n=int(input())
    dq=deque(input().strip('['']').split(','))
    isReverse=False
    isError=False

    if n==0:
     dq=deque()
    for c in command:
        if c=='R':
            isReverse= not isReverse
        elif c=='D':
            if len(dq)==0:
                print('error')
                isError=True
                break
            elif isReverse:
                dq.pop()
            else: 
                dq.popleft()
    if not isError:
        if isReverse:
            dq.reverse()     
        print("[" + ",".join(dq) + "]")