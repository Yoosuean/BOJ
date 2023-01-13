#BOJ 2751 수 정렬하기 2
import sys
import heapq as hq
input=sys.stdin.readline

n=int(input())
arr=[]

for _ in range(n):
    hq.heappush(arr,int(input()))
for _ in range(n):
    print(hq.heappop(arr))
