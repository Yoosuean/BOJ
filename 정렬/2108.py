#BOJ 2108 통계학
import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
num=[int(input()) for _ in range(n)]

#산술평균
print(round(sum(num)/len(num)))

#중앙값
num.sort()
print(num[len(num)//2])

#최빈값
cnt_num=Counter(num).most_common(2)
if  len(num)>1 and cnt_num[0][1]==cnt_num[1][1]:
    print(cnt_num[1][0])
else:
    print(cnt_num[0][0])

#범위
print(num[-1]-num[0])