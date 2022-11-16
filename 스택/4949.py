import sys

arr=[]
while True:
    c=sys.stdin.readline().rstrip()
    if c=='.':
        break;
    arr.append(c)


for i in arr:
    a=[] 
    for j in i:
        if j=='(':
            a.append('(')
        elif j==')':
            if a and a[-1]=='(':
                a.pop()
            else:
                print("no")
                break;
        if j=='[':
            a.append('[')
        elif j==']':
            if a and a[-1]=='[':
                a.pop()
            else:
                print("no")
                break;
    else:
        if not a:
            print("yes")
        else:
            print("no")