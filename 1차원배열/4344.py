#BOJ 4344 평균은 넘겠지
import sys
input=sys.stdin.readline
c=int(input())
for _ in range(c):
    cnt=0
    nums=list(map(int,input().split()))
    avg=sum(nums[1:])/nums[0]
    for i in nums[1:]:
        if i>avg:
            cnt+=1
    res=(cnt/nums[0])*100
    print(f'{res:.3f}%')