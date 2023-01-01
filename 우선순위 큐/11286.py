#BOJ 11286 절댓값 힙
import sys
import heapq as hq
input=sys.stdin.readline

n=int(input())
arr=[]

for _ in range(n):
    x=int(input())
    if x:
        hq.heappush(arr,(abs(x),x))
    else:
        if not arr:
            print(0)
        else:
            print(hq.heappop(arr)[1])
        