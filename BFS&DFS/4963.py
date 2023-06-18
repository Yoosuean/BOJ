#BOJ 4963 섬의 개수
from collections import deque

dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,-1,0,1,1,-1,1,-1]

def bfs(x,y,board):
    queue=deque([[x,y]])
    board[x][y]=2

    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or nx>=b or ny<0 or ny>=a:
                continue
            if board[nx][ny]==1:
                board[nx][ny]=2
                queue.append((nx,ny))

a=0
b=0
cnt=0
while True:
    board=[]
    a,b=map(int,input().split())
    if a+b==0:
        break
    for _ in range(b):
        board.append(list(map(int,input().split())))
    for i in range(b):
        for j in range(a):
            if board[i][j]==1:
                bfs(i,j,board)
                cnt+=1
    print(cnt)
