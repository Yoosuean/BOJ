#BOJ 11724 연결 요소의 개수
import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph,visited,v):
    queue=deque([v])
    visited[v]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if visited[i]: continue
    bfs(graph,visited,i)
    cnt+=1
print(cnt)



# #DFS
# import sys
# sys.setrecursionlimit(5000)
# input=sys.stdin.readline

# def dfs(graph,visited,v):
#     visited[v]=True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,visited,i)
    
# n,m=map(int,input().split())
# graph=[[] for _ in range(n+1)]
# visited=[False]*(n+1)
# cnt=0

# for _ in range(m):
#     a,b=map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(1,n+1):
#     if visited[i]: continue
#     dfs(graph,visited,i)
#     cnt+=1
# print(cnt)