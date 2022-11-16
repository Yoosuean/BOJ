# 스택개념 사용 코드
import sys

n=int(sys.stdin.readline())

for _ in range(n):
    stack=[]
    string=list(sys.stdin.readline())
    for ch in string:
        if ch == '(':
            stack.append('(')
        elif ch==')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break;
    else:
        if not stack:
                print("YES")   
        else:   
            print("NO")
        
        
        
    