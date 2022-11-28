import sys
k = int(input())
arr=[]

for i in range(6):
    dir,len = map(int, sys.stdin.readline().split())
    arr.append(len)

square_a = max(arr[0:6:2]) * max(arr[1:6:2])
square_b = arr[(arr.index(max(arr[0:6:2]))+3)%6] * arr[(arr.index(max(arr[1:6:2]))+3)%6]
print(k*(square_a-square_b))