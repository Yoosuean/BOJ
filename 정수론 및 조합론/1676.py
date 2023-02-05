#BOJ 1676 팩토리얼 0의 개수
n=int(input())
count=0
while n>1:
    count+=n//5
    n=n//5
print(count)