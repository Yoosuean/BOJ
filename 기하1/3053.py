#BOJ 3053 택시기하학
import math
r=int(input())
# 유클리드 기하학 원의 넓이: pi*r^2
# 택시 기하학 원의 넓이: 2*r^2
print('%.6f\n%.6f' %(r*r*math.pi,r*r*2))