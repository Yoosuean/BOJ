#BOJ 5639 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)

tree=[]
while True:                            
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break
        
def postorder(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if tree[s] < tree[i]:
            mid = i
            break

    postorder(s+1, mid-1) #왼쪽
    postorder(mid, e) #오른쪽
    print(tree[s])

postorder(0, len(tree)-1)