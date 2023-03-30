#BOJ 25192 인사성 밝은 곰곰이
N=int(input())
user=set()
cnt=0

for _ in range(N):
    tmp=input()
    if tmp=='ENTER':
        user.clear()
    elif tmp not in user:
        user.add(tmp)
        cnt+=1
print(cnt)

