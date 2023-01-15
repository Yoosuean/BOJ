#BOJ 25305 커트라인
n,k=map(int,input().split())
l=list(map(int,input().split()))
print(sorted(l)[-k])