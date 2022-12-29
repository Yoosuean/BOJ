#BOJ 16139 인간-컴퓨터 상호작용
import sys
input=sys.stdin.readline

s=list(input())
n=int(input())
arr=[]
li=[0]*26

for c in s:
    if 97<=ord(c)<=122:
        li[ord(c)-97]+=1
        arr.append(li[:])

for _ in range(n):
    c, start, end=input().split()
    res=arr[int(end)][ord(c)-97]
    if start !='0':
        res-=arr[int(start)-1][ord(c)-97]
    print(res)