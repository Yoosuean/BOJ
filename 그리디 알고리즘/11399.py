n=int(input())
times=list(map(int,input().split()))
times.sort()
min=0

for i in range(1,n+1):
    min+=sum(times[:i])


print(min)