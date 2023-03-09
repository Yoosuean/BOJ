#BOJ 9095 1,2,3 더하기
t=int(input())
dp=[0]*1001

dp[0]=1

for _ in range(t):
    n=int(input())
    for i in range(1,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])