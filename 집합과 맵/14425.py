#BOJ 14425 문자열 집합
import sys
n,m=map(int,sys.stdin.readline().split())
s=set(sys.stdin.readline() for _ in range(n))
count=0
for _ in range(m):
    data=sys.stdin.readline()
    if data in s:
        count+=1
print(count)