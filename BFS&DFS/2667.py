#BOJ 2667 단지번호붙이기
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(graph,x,y):
    queue=deque([[x,y]])
    graph[x][y]=0
    cnt=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                cnt+=1
    return cnt

n=int(input())
graph=[]
cnt_list=[]
for _ in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt_list.append(bfs(graph,i,j))
cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)





