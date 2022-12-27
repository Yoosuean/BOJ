#BOJ 2559 수열
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
nums=list(map(int,input().split()))
k_list=[]

k_list.append(sum(nums[:k]))

for i in range(n - k):
    k_list.append(k_list[i] - nums[i] + nums[k+i])

print(max(k_list))