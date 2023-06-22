#BOJ 13909 창문 닫기
n=int(input())
r=0
c=1
while(c<=n):
    r+=1
    c=(r+1)**2
print(r)