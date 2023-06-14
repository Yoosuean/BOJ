#BOJ 7562 나이트의 이동
from collections import deque

# x,y
position=[(-1,2),(-2,1),(1,2),(2,1),(-2,-1),(-1,-2),(2,-1),(1,-2)]

def bfs(x,y,dx,dy,visited):
    queue=deque([[x,y]])
    visited[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in position:
            nx=x+i[0]
            ny=y+i[1]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                if nx==dx and ny==dy:
                    print(visited[nx][ny]-1)
                    return True
                else:
                    queue.append((nx,ny))
    return False
                

t=int(input())

for _ in range(t):
    n=int(input())
    visited=[[0]*n for _ in range(n)]
    x,y=map(int,input().split())
    dx,dy=map(int,input().split())
    if not bfs(x,y,dx,dy,visited):
        print(0)
