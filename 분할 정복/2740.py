#BOJ 2740 행렬 곱셈
import sys
input=sys.stdin.readline
n,ma=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
mb,k=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(mb)]

res=[[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
            res[i][j]=sum([a[i][k]*b[k][j] for k in range(ma)])
    print(" ".join(map(str,res[i])))