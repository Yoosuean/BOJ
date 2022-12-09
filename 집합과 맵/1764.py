#BOJ 1764 듣보잡
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

a_set=set(input() for _ in range(n))
b_set=set(input() for _ in range(m))
res=list(a_set&b_set)
res.sort()
print(len(res))
for i in res:
    print(i.rstrip('\n'))