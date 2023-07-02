#BOJ 2583 영역구하기
from collections import deque
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            nx=x+dx
            ny=y+dy
            if (0 <= ny < m) and (0 <= nx < n) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx))
                cnt += 1
    return cnt
    
m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i, j))
print(len(res))
print(*sorted(res))