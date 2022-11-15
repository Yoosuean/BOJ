import sys

k=int(sys.stdin.readline())
arr=list()

for _ in range(k):
    num=int(sys.stdin.readline())
    if num==0:
        del arr[-1]
    else:
        arr.append(num)

print(sum(arr))