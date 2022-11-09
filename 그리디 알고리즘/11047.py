n, k=map(int, input().split()) 
coins=[]
min=0
for i in range(n):
    coins.append(int(input()))

coins.reverse()

for i in range(n):
    min += k//coins[i]
    k = k%coins[i] 

print(min)
