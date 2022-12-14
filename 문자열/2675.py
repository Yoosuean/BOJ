#BOJ 2675 문자열 반복
n=int(input())

for _ in range(n):
    cnt,word=input().split()
    for i in word:
        print(i*int(cnt),end='')
    print()

