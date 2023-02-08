#BOJ 11050 이항 계수 1
#dp로 풀어보기
from math import factorial
n,k=map(int,input().split())
print(factorial(n)//(factorial(n-k)*factorial(k)))