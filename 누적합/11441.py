#BOJ 11441 합 구하기
n=int(input())
nums=list(map(int,input().split()))
m=int(input())
prefix_sum=[0]
nums_sum=0
for i in range(n):
    nums_sum+=nums[i]
    prefix_sum.append(nums_sum)

for _ in range(m):
    res=0
    a,b=map(int,input().split())
    res+=prefix_sum[b]-prefix_sum[a-1]
    print(res)