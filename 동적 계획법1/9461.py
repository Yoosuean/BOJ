#BOJ 9461 파도반 수열

def res(n):
    dp[1]=1
    dp[2]=1
    dp[3]=1
    
    for i in range(4,n+1):
        dp[i]=dp[i-2]+dp[i-3]
    return dp[n]

t=int(input())
dp=[0]*101

for i in range(t):
    n=int(input())
    print(res(n))