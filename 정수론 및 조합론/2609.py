#BOJ 2609 최대공약수와 최소공배수
import math
a,b=map(int,input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))

# # 유클리드 호제법
# def gcd(a,b):
#     while b>0:
#         a,b=b,a%b
#     return a

# def lcm(a,b):
#     return a*b//gcd(a,b)

# print(gcd(a,b))
# print(lcm(a,b))