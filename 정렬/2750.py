#BOJ 2750 수 정렬하기
n=int(input())
arr=[int(input()) for _ in range(n)]
arr.sort()
for i in arr:
    print(i)
