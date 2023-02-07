#BOJ 1010 다리놓기
from math import factorial
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    ans=factorial(b)//(factorial(b-a)*factorial(a))
    print(ans)