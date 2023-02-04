#BOJ 11650 좌표 정렬하기
import sys
input=sys.stdin.readline
n=int(input())
nums=[]
for _ in range(n):
    nums.append(list(input().split()))
nums.sort(key=lambda num: (num[0], num[1]))

for num in nums:
    print(num[0],num[1])