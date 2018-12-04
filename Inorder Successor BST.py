# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ans = self.inorder(root, p, None)
        if ans[0]:
            return ans[1]
        else:
            return None
        
        
    def inorder(self, node, p, prev):
        ans_left = (False, None)
        if node.left:
            ans_left = self.inorder(node.left, p, prev)
        elif prev and p.val == prev.val:
            return (True, node) 
        if ans_left[0]:
            return ans_left
        elif ans_left[1] and ans_left[1].val == p.val:
            return (True, node)
        ans_right=(False, None)
        if node.right:
            ans_right = self.inorder(node.right,p,node)
        if ans_right[0]:
            return ans_right
        elif ans_right[1]:
            if ans_right[1].val > node.val:
                return (False, ans_right[1])
            else:
                return (False, node)
        else:
            return (False, node)

solution = Solution()


node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)
node7=TreeNode(7)
node8=TreeNode(8)
node9=TreeNode(9)
node10=TreeNode(10)
node11=TreeNode(11)
node12=TreeNode(12)
node13=TreeNode(13)
node14=TreeNode(14)
node15=TreeNode(15)

node2.left = node1
node2.right = node3
print(solution.inorderSuccessor(node2, node1) == node2)

node5.left=node3
node5.right=node6
node3.left=node2
node3.right=node4
node2.left=node1
node2.right=None
print(solution.inorderSuccessor(node5, node6) == None)
print(solution.inorderSuccessor(node5, node1) == node2)
print(solution.inorderSuccessor(node5, node2) == node3)
print(solution.inorderSuccessor(node5, node3) == node4)
print(solution.inorderSuccessor(node5, node4) == node5)
print(solution.inorderSuccessor(node5, node5) == node6)


node5.left=node3
node5.right=node7
node3.left=node2
node3.right=node4
node2.left=node1
node2.right=None
node7.left=node6
node7.right=node9
node9.left=node8
print(solution.inorderSuccessor(node5, node1) == node2)
print(solution.inorderSuccessor(node5, node2) == node3)
print(solution.inorderSuccessor(node5, node3) == node4)
print(solution.inorderSuccessor(node5, node4) == node5)
print(solution.inorderSuccessor(node5, node5) == node6)
print(solution.inorderSuccessor(node5, node6) == node7)
print(solution.inorderSuccessor(node5, node7) == node8)
print(solution.inorderSuccessor(node5, node8) == node9)
print(solution.inorderSuccessor(node5, node9) == None)

node8.left=node4
node8.right=node12
node4.left=node2
node4.right=node6
node2.left=node1
node2.right=node3
node3.left=None
node3.right=None
node6.left=node5
node5.left=None
node5.right=None
node6.right=node7
node7.left=None
node7.right=None

node12.left=node10
node10.left=node9
node9.left=None
node10.right=node11
node12.right=node14
node14.left=node13
node14.right=node15
print(solution.inorderSuccessor(node8, node1) == node2)
print(solution.inorderSuccessor(node8, node2) == node3)
print(solution.inorderSuccessor(node8, node3) == node4)
print(solution.inorderSuccessor(node8, node4) == node5)
print(solution.inorderSuccessor(node8, node5) == node6)
print(solution.inorderSuccessor(node8, node6) == node7)
print(solution.inorderSuccessor(node8, node7) == node8)
print(solution.inorderSuccessor(node8, node8) == node9)
print(solution.inorderSuccessor(node8, node9) == node10)
print(solution.inorderSuccessor(node8, node10) == node11)
print(solution.inorderSuccessor(node8, node11) == node12)
print(solution.inorderSuccessor(node8, node12) == node13)
print(solution.inorderSuccessor(node8, node13) == node14)
print(solution.inorderSuccessor(node8, node14) == node15)
print(solution.inorderSuccessor(node8, node15) == None)


node3.left=node2
node3.right=node4
node2.left=node1
node2.right=None

node4.left=None
node4.right=node5
node5.left=None
node5.right=None
print(solution.inorderSuccessor(node3, node1) == node2)
print(solution.inorderSuccessor(node3, node2) == node3)
print(solution.inorderSuccessor(node3, node3) == node4)
print(solution.inorderSuccessor(node3, node4) == node5)
print(solution.inorderSuccessor(node3, node5) == None)



