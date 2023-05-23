#BOJ 2178 미로탐색
from collections import deque

#좌상우하
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    global graph
    queue=deque([(x,y)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    print(graph[n-1][m-1])

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
bfs(0,0)
