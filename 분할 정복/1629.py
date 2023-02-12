#BOJ 1629 곱셈

# pow(a,b)%c -> 시간초과
# pow(a,b,c) -> 통과

## 분할정복 풀이
# 10^11%12
# ((10^5)%12*(10^5)%12*10)%12
# ((10^2)%12*(10^2)%12*10)%12

def solution(a,b):
    if b==1:
        return a%c
    elif b==2:
        return a*a%c
    else:
        d=solution(a,b//2)
        if b%2==0:
            return (d*d)%c
        else:
            return (d*d*a)%c

a,b,c=map(int,input().split())
print(solution(a,b))