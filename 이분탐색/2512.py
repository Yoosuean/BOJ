#BOJ 2512 예산

N=int(input())
city=list(map(int,input().split()))
M=int(input())

start,end=0,max(city)

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in city:
        if i>mid:
            sum+=mid
        else:
            sum+=i
    if sum<=M:
        start=mid+1
    else:
        end=mid-1
print(end)