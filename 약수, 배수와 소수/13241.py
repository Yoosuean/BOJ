#BOJ 13241 최소공배수

a, b = map(int, input().split())

def gcd(a, b):
    while b:
        mod=b
        b=a%b
        a=mod
    return a

print(a*b//gcd(a,b))