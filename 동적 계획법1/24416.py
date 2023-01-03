#BOJ 24416 알고리즘 수업 - 피보나치 수 1
def fib(n):
    global cnt_fib
    if n==1 or n==2:

        return 1
    else:
        cnt_fib+=1
        return fib(n-1)+fib(n-2)

def dpFib(n):
    global cnt_dpFib
    if n in arr:
        return arr[n]
    else:
        arr[n]=dpFib(n-1)+dpFib(n-2)
        cnt_dpFib+=1
        return arr[n]

n=int(input())
cnt_fib,cnt_dpFib=1,0
arr={1:1,2:1}
fib(n)
dpFib(n)
print(cnt_fib,cnt_dpFib,sep=' ')