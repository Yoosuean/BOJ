#BOJ 11051 이항 계수 2
#dp로 풀어보기
from math import factorial
n,k=map(int,input().split())
c=factorial(n)//(factorial(n-k)*factorial(k))
print(c%10007)