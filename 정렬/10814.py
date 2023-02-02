#BOJ 10814 나이순 정렬
n=int(input())
user=[]
for _ in range(n):
    user.append(list(input().split()))

user.sort(key = lambda age:int(age[0]))

for i in user:
    print(" ".join(i))