#BOJ 11650 좌표 정렬하기
import sys
input=sys.stdin.readline
n=int(input())
nums=[]
for _ in range(n):
    nums.append(list(input().split()))
nums.sort(key=lambda num: (int(num[0]), int(num[1])))
# num 값을 문자열로 정렬하면 101보다 11이 크다고 판단, 꼭 정수로 바꿔주기
for num in nums:
    print(num[0],num[1])