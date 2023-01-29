#BOJ 15649 N과 M(1)
N, M=map(int, input().split())
ans=[]

def back():
    if len(ans)==M:
        print(" ".join(map(str, ans)))
        return 
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()      
back()

# ** itertools 사용
# from itertools import permutations
# n,m=map(int,input().split())
# arr=list(range(1,n+1))
# for i in permutations(arr,m):
#     print(" ".join(map(str,i)))