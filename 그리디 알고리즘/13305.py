citys=int(input()) #도시의 개수
roads=list(map(int,input().split())) #도로의 길이 3개
costs=list(map(int,input().split())) #주유소의 리터당 가격 4개 

res=0
min=costs[0]

for i in range(citys-1):
    if min>costs[i]:
        min=costs[i]
    res+=min*roads[i]
print(res)