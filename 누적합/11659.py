#BOJ 11659 누적합
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
nums=list(map(int,input().split()))
nums_sum=[0]
sum=0

for i in range(n):
    sum+=nums[i]
    nums_sum.append(sum)

for _ in range(m):
    start,end=map(int,input().split())
    print(nums_sum[end]-nums_sum[start-1])
    