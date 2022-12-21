#BOJ 2805 나무자르기
n,m=map(int,input().split())
trees=list(map(int,(input().split())))

start=1
end=max(trees)

while start<=end:
    mid=(start+end)//2
    sum=0
    for tree in trees:
        if mid<=tree:
            sum+=tree-mid
    if sum>=m:
        start=mid+1
    else:
        end=mid-1
print(end)
