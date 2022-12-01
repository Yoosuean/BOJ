#BOJ 1110 더하기 사이클
n=int(input())
count=0
c=n
while True:
    a=c//10
    b=c%10
    c=b*10+(a+b)%10
    count+=1
    if c==n:
        break
print(count)