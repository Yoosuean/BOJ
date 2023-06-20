#BOJ 19941 햄버거 분배
n,k = map(int, input().split())
place=list(input())
res= 0
for i in range(n):
    if place[i] == 'P':
        for i in range(max(i-k, 0),min(i+k+1, n)):
            if place[i]=='H':
                place[i] = 0
                res+= 1
                break
print(res)