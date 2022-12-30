#BOJ 11279 최대 힙
import sys
input=sys.stdin.readline

n=int(input())
arr=[0]
for _ in range(n):
    x=int(input())
    arr.append(x)
    if x==0:
        m=max(arr)
        print(m)
        arr.remove(m)