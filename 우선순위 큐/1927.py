#BOJ 1927 최소 힙
import sys
import heapq as hq
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    x=int(input())
    if x:
        hq.heappush(arr,x)
    else:
        if len(arr)>=1:
            print(hq.heappop(arr))
        else:
            print(0) 