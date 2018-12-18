# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1 2 3 4 5 7 6 8 9 10
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        class Pointer:
            def __init__(self):
                self.left = None
                self.middle = None
                self.right = None
                self.prev = None
        pointer = Pointer()
        self.inorderTraversal(root, pointer)
        if pointer.left and pointer.right:
            self.swap(pointer.left, pointer.right)
        elif pointer.left and pointer.middle:
            self.swap(pointer.left, pointer.middle)
    
    def inorderTraversal(self, node, pointer):
        if node.left:
            self.inorderTraversal(node.left, pointer)
        
        if pointer.prev and pointer.prev.val >= node.val:
            if not pointer.left:
                pointer.left = pointer.prev
                pointer.middle = node
            elif not pointer.right:
                pointer.right = node
        pointer.prev = node   
        if node.right:
            self.inorderTraversal(node.right, pointer)

    def swap(self, a, b):
        tmp = a.val
        a.val = b.val
        b.val = tmp
        
        
    

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left=node3
node3.right=node2

solution = Solution()
solution.recoverTree(node1)