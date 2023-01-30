#BOJ 15651 N과 M (3)
n,m=map(int,input().split())
ans=[]

def back():
    if len(ans)==m:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,n+1):
        ans.append(i)
        back()
        ans.pop()
back()

# ** itertools 사용
# from itertools import product
# n,m=map(int,input().split())
# arr=list(range(1,n+1))
# for i in product(arr,repeat=m):
#     print(" ".join(map(str,i)))