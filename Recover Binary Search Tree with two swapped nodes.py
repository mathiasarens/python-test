# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1 2 3 4 5 7 6 8 9 10
class Solution:
    def __init__(self):
        self.left = None
        self.middle = None
        self.right = None
        self.prev = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorderTraversal(root)
        if self.left and self.right:
            self.swap(self.left, self.right)
        elif self.left and self.middle:
            self.swap(self.left, self.middle)
    
    def inorderTraversal(self, node):
        if node.left:
            self.inorderTraversal(node.left)
        
        if self.prev and self.prev.val >= node.val:
            if not self.left:
                self.left = self.prev
                self.middle = node
            elif not self.right:
                self.right = node
        self.prev = node   
        if node.right:
            self.inorderTraversal(node.right)

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