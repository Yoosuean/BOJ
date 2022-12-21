#BOJ 1654 랜선자르기
import sys

k,n=map(int,input().split())
lines=[int(sys.stdin.readline()) for _ in range(k)]

start=1
end=max(lines)

while start<=end:
    mid=(start+end)//2
    count=0
    for i in lines:
        count+=i//mid
    if count>=n:
        start=mid+1
    else:
        end=mid-1
print(end)

