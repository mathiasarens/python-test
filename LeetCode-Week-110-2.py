# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.levelOrder(root, L, R, 0)
        
    def levelOrder(self, node, L, R, sum):
        if node.left:
            sum = self.levelOrder(node.left, L, R, sum)

        if node.val >= L and node.val <= R:
            sum += node.val
        if node.val == R:
            return sum
        
        if node.right:
            sum = self.levelOrder(node.right, L, R, sum)
        
        return sum
        
node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = 
solution = Solution()
# print(solution.rangeSumBST())
# print()