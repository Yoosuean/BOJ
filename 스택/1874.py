
import sys

n=int(sys.stdin.readline())
stack=[]
arr=[]
isOver=False
count=1

for _ in range(n):
    num=int(sys.stdin.readline())
    while count<=num:
        stack.append(count)
        arr.append('+')
        count+=1
    if stack[-1]==num:
        arr.append('-')
        stack.pop()
    else:
        isOver=True
if isOver:
    print('NO')
else:
    for i in arr:
        print(i)