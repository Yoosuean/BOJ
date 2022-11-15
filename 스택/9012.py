import sys

n=int(sys.stdin.readline())
arr=[]

for _ in range(n):
    count=0
    arr=list(sys.stdin.readline())
    if arr[0]==')':
        print('NO')
        continue;
    else:
        for i in range(len(arr)-1):
            if arr[i]=='(':
                count+=1
            else:
                count-=1
                if count<0:
                    break;
    if count==0:
        print('YES')
    else:
        print('NO')
        
        
        
    