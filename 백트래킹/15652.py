#BOJ 15652 n과 m (4)
n,m=map(int,input().split())
ans=[]

def back(start):
    if len(ans)==m:
        print(" ".join(map(str,ans)))
        return
    for i in range(start,n+1):
        ans.append(i)
        back(i)
        ans.pop()
back(1)

# ** itertools 사용
# from itertools import combinations_with_replacement
# n,m=map(int,input().split())
# arr=list(range(1,n+1))
# for i in combinations_with_replacement(arr,m):
#     print(" ".join(map(str,i)))