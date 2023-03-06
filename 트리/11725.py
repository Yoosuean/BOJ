#BOJ 11725 트리의 부모 찾기
from collections import deque
N = int(input())
res = [i for i in range(N+1)]
arr = [list() for _ in range(N+1)]

for _ in range(N-1):
    try:
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    except EOFError:
        break

queue = deque([1])
res[1] = 0
while queue:
    node = queue.popleft()
    for n in arr[node]:
        if res[n] == n:
            queue.append(n)
            res[n] = node

print("\n".join(map(str,res[2:])))
