#BOJ 10026 적록색약
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(board,x,y):
    curr=board[x][y]
    queue=deque([(x,y)])
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=n or nx<0 or ny>=n or ny<0:
                continue
            if not visited[nx][ny] and board[nx][ny]==curr:
                visited[nx][ny]=True
                queue.append((nx,ny))

n=int(input())
board=[]
cnt1=0
cnt2=0
board=[list(input()) for _ in range(n)]

# 적록색약이 아닌 사람
visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(board,i,j)
            cnt1+=1

#적록색약인 사람
for i in range(n):
    for j in range(n):
        if board[i][j]=='G':
            board[i][j]='R'

visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
                bfs(board,i,j)
                cnt2+=1
print(cnt1,cnt2)