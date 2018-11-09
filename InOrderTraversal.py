# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversalForNode(self, node):
        result = []
        if node is None:
            return result
        if node.left is not None:
            result.extend(self.inorderTraversal(node.left))
        result.append(node.val)
        if node.right is not None:
            result.extend(self.inorderTraversal(node.right))
        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversalForNode(root)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))