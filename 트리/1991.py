#BOJ 1991 트리순회
n=int(input())
tree={}
for i in range(n):
    root, left, right=input().split()
    tree[root]=[left,right]

#전위
def preorder(root):
    if root=='.':
        return
    else:
        print(root,end="")
        preorder(tree[root][0])
        preorder(tree[root][1])

#중위
def inorder(root):
    if root=='.':
        return
    else:
        inorder(tree[root][0])
        print(root,end="")
        inorder(tree[root][1])

#후위
def postorder(root):
    if root=='.':
        return
    else:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')