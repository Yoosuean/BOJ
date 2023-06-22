#BOJ 2563 색종이

n=int(input())
arr=[[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    a,b=map(int,input().split())
    
    for i in range(a,a,+10):
        for j in range(b,b+10):
            arr[i][j]=1
cnt=0
for row in arr:
    cnt+=row.count(1)
print(cnt)
        