#BOJ 2485 가로수
import sys
from math import gcd

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())

arr = []

for i in range(n-1):
    num=int(sys.stdin.readline())
    arr.append(num-a)
    a=num

g=arr[0]
for j in range(1,len(arr)):
    g=gcd(g,arr[j])

res=0
for each in arr:
    res+=each//g-1
print(res)