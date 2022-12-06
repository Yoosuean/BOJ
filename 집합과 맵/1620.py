#BOJ 1620 나는야 포켓몬 마스터 이다솜
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
monsters={}
for i in range(1,n+1):
    name=input().rstrip()
    monsters[i]=name
    monsters[name]=i

for _ in range(m):
    q=input().rstrip()
    if q.isdigit():
        print(monsters[int(q)])
    else:
        print(monsters[q])