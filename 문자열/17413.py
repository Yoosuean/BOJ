#BOJ 17413 단어 뒤집기 2
import sys
input=sys.stdin.readline
s=input().rstrip()+' '
stack=[] 
result=''
isbracket=False

for i in s : 
    if i=='<': 
        isbracket=True
        for _ in range(len(stack)):
            result+=stack.pop()
    stack.append(i)

    if i=='>':
        isbracket=False 
        for _ in range(len(stack)): 
            result+=stack.pop(0)

    if i==' ' and not isbracket: 
        stack.pop() 
        for _ in range(len(stack)): 
            result+=stack.pop()
        result += ' '
print(result)
