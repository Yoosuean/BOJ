#BOJ 2170 스위핑
import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()

start=arr[0][0]
end=arr[0][1]
cnt=0

for i in range(1,n):
    if arr[i][0]<=end<arr[i][1]:
        end=arr[i][1]
    elif arr[i][0]>end:
        cnt+=end-start
        start=arr[i][0]
        end=arr[i][1]
cnt+=end-start
print(cnt)

