#BOJ 2110 공유기 설치
import sys
n,c=map(int,input().split())
arr=[int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

start=1
end=arr[-1]-arr[0]
res=0


while start<=end:
    mid=(start+end)//2
    cnt=1
    current=arr[0]
    for i in range(1,len(arr)):
        if arr[i] >= current+mid:
            cnt+= 1
            current=arr[i]
    if cnt>=c:
        start = mid + 1
        res=mid
    else:
        end = mid - 1
print(res)