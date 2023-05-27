#BOJ 1238 파티
#다익스트라
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

def dijkstra(start,distance):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance1=[INF]*(n+1)
for _ in range(m):
    a,b,t=map(int,input().split())
    graph[a].append((b,t))

dijkstra(x,distance1)
distance2=[]
distance_list=[]
cost=[]
for i in range(n):
    distance2=[INF]*(n+1)
    distance_list.append(dijkstra(x,distance2))

for i in range(1,n+1):
    cost.append(distance1[i]+distance2)
