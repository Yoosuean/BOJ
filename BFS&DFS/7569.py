#BOJ 7569 토마토
from collections import deque

#위, 아래, 왼쪽, 오른쪽, 앞, 뒤
directions=[(0,0,1),(0,0,-1),(-1,0,0),(1,0,0),(0,1,0),(0,-1,0)]


# 3차원 BFS !!
def bfs():
    while queue:
        z,x,y=queue.popleft()
        for i in range(6):
            nx=x+directions[i][0]
            ny=y+directions[i][1]
            nz=z+directions[i][2]
            if nx<0 or nx>=n or ny<0 or ny>=m or nz<0 or nz>=h:
                continue
            if boxs[nz][nx][ny]==0:
                boxs[nz][nx][ny]=boxs[z][x][y]+1
                queue.append((nz,nx,ny))


m,n,h=map(int,input().split())
boxs=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
queue=deque()
is_complete=True
cnt=0


for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxs[i][j][k]==1:
                queue.append((i,j,k))

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxs[i][j][k]==0:
                is_complete=False
            cnt=max(cnt,boxs[i][j][k])
if is_complete:
    print(cnt-1)
else:
    print(-1)