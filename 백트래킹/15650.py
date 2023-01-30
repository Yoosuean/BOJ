#BOJ 15650 N과 M (2)
N, M=map(int, input().split())
ans=[]

def back(start):
    if len(ans)==M:
        print(" ".join(map(str, ans)))
        return 
    for i in range(start, N+1):
        if i not in ans:
            ans.append(i)
            back(i+1)
            ans.pop()      
back(1)

# ** itertools 사용
# from itertools import combinations
# n,m=map(int,input().split())
# arr=list(range(1,n+1))
# for i in combinations(arr,m):
#     print(" ".join(map(str,i)))