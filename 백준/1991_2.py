N = int(input())
tree = list([0] * 2 for _ in range(N + 1)) # 왼쪽 자식, 오른쪽 자식 

for i in range(N): 
    temp = list(input().split()) 
    root = ord(temp[0]) - 64 
    left = ord(temp[1]) - 64 
    right = ord(temp[2]) - 64 
    
    if left == -18 and right != -18: # 첫번째 자식은 없고, 두번째 자식이 있으면 
        tree[root][0] = 0 
        tree[root][1] = right 
    
    elif left != -18 and right == -18: # 첫번째 자식은 있고, 두번째 자식만 없으면 
        tree[root][0] = left 
        tree[root][1] = 0 
        
    elif left == -18 and right == -18: # 두 자식 다 없으면 
        tree[root][0] = 0 
        tree[root][1] = 0 
    
    else: 
        tree[root][0] = left
        tree[root][1] = right


def pre_order(node): # 전위 순회 
    if node: 
        print(chr(node+64), end='') # 할 일 
        pre_order(tree[node][0]) # 왼쪽 자식 
        pre_order(tree[node][1]) # 오른쪽 자식 

def in_order(node): # 중위 순회 
    if node: 
        in_order(tree[node][0]) # 왼쪽 자식 
        print(chr(node+64), end='') # 할 일 
        in_order(tree[node][1]) # 오른쪽 자식 
        
def post_order(node): # 후위 순회 
    if node: 
        post_order(tree[node][0]) # 왼쪽 자식 
        post_order(tree[node][1]) # 오른쪽 자식 
        print(chr(node+64), end='') # 할 일 
        
pre_order(1) 
print() 
in_order(1) 
print() 
post_order(1)
