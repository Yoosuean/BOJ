#BOJ 1920 수 찾기

def binary_search(array,target,start,end):
    if start>end:
        return 0
    mid=(start+end)//2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n=int(input())
arr=list(map(int,input().split()))
m=int(input())
target=list(map(int,input().split()))
arr.sort()

for i in target:
    res=binary_search(arr,i,0,n-1)
    print(res)


    

