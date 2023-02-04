#BOJ 1427 소트인사이드
n=list(map(int,input().strip()))
n.sort(reverse=True)
for i in n:
    print(i,end="")