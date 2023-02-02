#BOJ 3036 링
n=int(input())
ring=list(map(int,input().split()))

for i in ring[1:]:
    a,b=ring[0],i
    for j in reversed(range(1,min(a,b)+1)):
        if a%j==0 and b%j==0:
            a//=j
            b//=j
            break
    print(a,b,sep='/')


