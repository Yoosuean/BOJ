#BOJ 9375 패션왕 신해빈
import sys
input=sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    clothes = {}
    for j in range(n):
        name, type = input().split()

        if type not in clothes.keys():
            clothes[type] = 1
        else:
            clothes[type] += 1
    res = 1
    for i in clothes: 
        res *= (clothes[i]+1) 
    print(res-1) 