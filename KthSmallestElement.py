'''Kth smallest element in the the bst can be found using inorder traversal'''

def kthsmallest(root,k):
    x = []

    def ino(node):
        if node:
            ino(node.left)
            x.append(node.val)
            ino(node.right)


    ino(root)
    return x[k-1]