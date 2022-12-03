#BOJ 1780 종이의 개수
import sys
n=int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 
a=b=c=0
def cut(x,y,n):
    global a, b, c
    num=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=paper[i][j]:
                new_n=n//3
                cut(x,y,new_n)
                cut(x,y+new_n, new_n)
                cut(x,y+new_n*2, new_n)
                cut(x+new_n,y,new_n)
                cut(x+new_n,y+new_n,new_n)
                cut(x+new_n,y+new_n*2,new_n)
                cut(x+new_n*2,y,new_n)
                cut(x+new_n*2,y+new_n,new_n)
                cut(x+new_n*2,y+new_n*2,new_n)
                return
    if num==-1:
        a+=1
    elif num==0:
        b+=1
    else:
        c+=1
cut(0,0,n)
print(a,b,c,sep='\n')