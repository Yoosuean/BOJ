#BOJ 18870 좌표 압축
import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
n_set=set(arr)
arr2=list(n_set)
arr2.sort()

n_dict={}
for i in range(len(arr2)):
    n_dict[arr2[i]]=i
for i in arr:
    print(n_dict[i], end=' ')