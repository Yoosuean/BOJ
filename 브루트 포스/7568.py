#BOJ 7568 덩치
n=int(input())
arr=[]
res=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    count=1
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count+=1
    res.append(count)

for num in res:
    print(num,end=' ')