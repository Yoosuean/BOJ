#BOJ 10986 나머지합
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
sum=0
r=[0]*m

for i in range(n):
    sum+=num[i]
    r[sum%m]+=1
result=r[0]
for i in r:
    result+=i*(i-1)//2
print(result)