N = int(input())
tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]
 
 
def preorder(root): #전위
    if root != '.':
        print(root, end='')  
        preorder(tree[root][0]) 
        preorder(tree[root][1]) 
 
def inorder(root): #중위
    if root != '.':
        inorder(tree[root][0]) 
        print(root, end='') 
        inorder(tree[root][1])  
 
 
def postorder(root): #후위
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1]) 
        print(root, end='') 
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')