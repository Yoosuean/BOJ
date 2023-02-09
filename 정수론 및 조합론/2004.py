#BOJ 2004 조합 0의 개수
n,m=map(int,input().split())

def cnt_two(n):
    cnt2=0
    while n!=0:
        n=n//2
        cnt2+=n
    return cnt2

def cnt_five(n):
    cnt5=0
    while n!=0:
        n=n//5
        cnt5+=n
    return cnt5
print(min(cnt_two(n)-cnt_two(m)-cnt_two(n-m), cnt_five(n)-cnt_five(m)-cnt_five(n-m)))
    