#BOJ 2231 분해합
n=int(input())
for i in range(1,n+1):
    num=sum((map(int,str(i))))
    res=i+num
    if res==n:
        print(i)
        break
    elif i==n:
        print(0)