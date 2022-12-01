#BOJ 11758 CCW
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

res = (x2-x1)*(y3-y2)-(x3-x2)*(y2-y1)

if res > 0:
    print(1)
elif res < 0:
    print(-1)
else:
    print(0)