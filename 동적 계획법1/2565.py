#BOJ 2565 전깃줄
import sys
input=sys.stdin.readline
arr=[]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))
arr.sort()

dp=[1]*n

for i in range(n):
    for j in range(i):
        if arr[i][1]>arr[j][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))