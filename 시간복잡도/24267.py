#BOJ 24267 알고리즘 수업 - 알고리즘의 수행 시간 6
n=int(input())
print(((n-2)*(n-1)*(2*n-3)+3*(n-1)*(n-2))//12)
print(3)

# 시간초과
# def MenOfPassion(n):
#     count=0
#     for i in range(1,n-1):
#         for j in range(i+1,n):
#             for k in range(j+1,n+1):
#                 count+=1
#     return count
# print(MenOfPassion(n))