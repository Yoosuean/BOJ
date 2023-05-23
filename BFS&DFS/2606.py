#BOJ 2606 바이러스
from collections import deque

def bfs(graph,v):
    global cnt
    queue=deque([v])
    while queue:
        v=queue.popleft()
        visitied[v]=True

        for i in graph[v]:
            if not visitied[i]:
                queue.append(i)
                visitied[i]=True
                cnt+=1
    print(cnt)

computer=int(input())
n=int(input())
graph=[[] for _ in range(computer+1)]
visitied=[False]*(computer+1)
cnt=0

for _ in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph,1)



# 처음코드
# from collections import deque

# def bfs(graph,start):
#     queue=deque([start])

#     while queue:
#         visited[start]=True
#         v=queue.popleft()

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True

# computer=int(input())
# connect=int(input())
# graph=[[] for _ in range(computer+1)]
# visited=[False]*(computer+1)

# #양방향
# for _ in range(connect):
#     a,b=map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# bfs(graph,1)
# print(visited.count(True)-1)
