#BOJ 25682 체스판 다시 칠하기 2
#시간초과 pypy 제출
import sys
input=sys.stdin.readline

def solution(color):
    dp=list([0]*(m+1) for i in range(n+1))
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                val=board[i][j]!=color
            else:
                val=board[i][j]==color
            dp[i+1][j+1]=dp[i][j+1]+dp[i+1][j]-dp[i][j]-val
        cnt=int(1e9)
        for i in range(1,n-k+2):
            for j in range(1,m-k+2):
                cnt=min(cnt,dp[i+k-1][j+k-1]-dp[i+k-1][j-1]-dp[i-1][j+k-1]+dp[i-1][j-1])
            return cnt



n,m,k=map(int,input().split())
board=[list(input() for _ in range(n))]
print(min(solution('W'),solution('B')))