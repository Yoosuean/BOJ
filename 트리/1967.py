#BOJ 1967 트리의 지름
import sys
sys.setrecursionlimit(10**6)

def DFS(node, weight):
    for n,w in tree[node]:
        if dis[n]==-1: # 방문확인
            dis[n]=weight+w
            DFS(n,weight+w)

n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

dis=[-1]*(n+1) # 가중치 합
dis[1]=0 # 루트노드, 가중치
DFS(1,0)

max_node=dis.index(max(dis)) # 가중치 합의 최대가 되는 노드
dis=[-1]*(n+1)
dis[max_node]=0 # 최대가 되는 노드부터 dfs 재수행
DFS(max_node,0)

print(max(dis))



