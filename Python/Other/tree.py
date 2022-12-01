import time

start = time.time()

class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    
    def __str__(self):
        return str(self.data)
        
def insert_tree(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert_tree(root.left, node)
        elif root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert_tree(root.right, node)

def sort_asc(root):
    if root != None:
        sort_asc(root.left)
        print(root.data)
        return sort_asc(root.right)
    return '---'

def sort_desc(root):
    if root != None:
        sort_desc(root.right)
        print(root.data)
        sort_desc(root.left)
    return '---'

def search_min(root):
    if root.left is None:
        return root.data
    else:
        return search_min(root.left)

def search_max(root):
    if root.right is None:
        return root.data
    else:
        return search_max(root.right)

def pre_order(root):
    if root != None:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)
    return '---'

def post_order(root):
    if root != None:
        post_order(root.left)
        post_order(root.right)
        print(root.data)
    return '---'

tree = Node(8)
insert_tree(tree, Node(1))
insert_tree(tree, Node(3))
insert_tree(tree, Node(6))
insert_tree(tree, Node(4))
insert_tree(tree, Node(7))
insert_tree(tree, Node(10))
insert_tree(tree, Node(14))
insert_tree(tree, Node(13))
insert_tree(tree, Node(10))

print(pre_order(tree))
print('--- {0} seconds ---'.format(time.time() - start))


