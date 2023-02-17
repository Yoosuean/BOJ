#BOJ 14888 연산자 끼워넣기
n=int(input())
num=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
maximum=-1e9
minimum=1e9

def back(add,sub,mul,div,sum,idx):
    global maximum, minimum
    if idx==n:
        maximum=max(maximum,sum)
        minimum=min(minimum,sum)
        return
    if add:
        back(add-1,sub,mul,div,sum+num[idx],idx+1)
    if sub:
        back(add,sub-1,mul,div,sum-num[idx],idx+1)
    if mul:
        back(add,sub,mul-1,div,sum*num[idx],idx+1)
    if div:
        back(add,sub,mul,div-1,int(sum/num[idx]),idx+1)
back(add,sub,mul,div,num[0],1)
print(maximum,minimum, sep='\n')