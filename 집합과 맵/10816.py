#BOJ 10816 숫자 카드2
import sys
input=sys.stdin.readline

n=input()
n_list=(map(int,input().split()))
m=input()
m_list=list(map(int,input().split()))
count={}
for i in n_list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for j in m_list:
    val=count.get(j)
    if val==None:
        print(0,end=' ')
    else:
        print(val,end=' ')