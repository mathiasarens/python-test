class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildNode(self, preorder, inorder):
        root_inorder_index = inorder.index(preorder[0])
        node = TreeNode(inorder[root_inorder_index])
        length_left = len(inorder[0:root_inorder_index])
        if length_left > 0:
            node.left = self.buildNode(preorder[1:1+length_left], inorder[0:root_inorder_index])
        length_right = len(inorder[root_inorder_index + 1:len(inorder)])
        if length_right > 0:
            node.right = self.buildNode(preorder[1+length_left:len(preorder)], inorder[root_inorder_index+1:len(inorder)])
        return node

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) < 1 or len(preorder) != len(inorder):
            return None
        return self.buildNode(preorder, inorder)


solution = Solution()
result = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
result = solution.buildTree([3], [3])
result = solution.buildTree([], [])
print(result)