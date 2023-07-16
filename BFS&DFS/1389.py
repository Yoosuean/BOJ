#BOJ 1389 케빈 베이컨의 6단계 법칙
from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                queue.append(i)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res=[]

for i in range(n):
    visited =[0]*(n + 1)
    bfs(i+1)
    res.append(sum(visited))

print(res.index(min(res)) + 1)