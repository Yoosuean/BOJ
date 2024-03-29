import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 

res=[]

def cut(x,y,n):
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2, n//2)
                cut(x+n//2,y, n//2)
                cut(x+n//2,y+n//2, n//2)
                return
    if color==0:
        res.append(0)
    else:
        res.append(1)

cut(0,0,n)
print(res.count(0))
print(res.count(1))
