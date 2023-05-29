from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y,n):
	global board
	queue=deque([(x,y)])
	board[x][y]=0
	cap=1
	while queue:
		x,y=queue.popleft()
		for i in range(4):
			nx=dx[i]+x
			ny=dy[i]+y
			if nx<0 or nx>=n or ny<0 or ny>=n:
				continue
			if board[nx][ny]==1:
				cap+=1
				board[nx][ny]=0
				queue.append((nx,ny))
	return cap

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
cnt=0
res=[]

for i in range(n):
	for j in range(n):
		if board[i][j]==1:
			tmp=bfs(i,j,n)
			res.append(tmp)
			cnt+=1
res.sort()			
print(cnt)
for i in res:
	print(i,end=' ')