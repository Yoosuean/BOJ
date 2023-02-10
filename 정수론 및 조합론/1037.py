#BOJ 1037 약수
n=int(input())
n_list=list(map(int,input().split()))
n_list.sort()
print(n_list[0]*n_list[-1])