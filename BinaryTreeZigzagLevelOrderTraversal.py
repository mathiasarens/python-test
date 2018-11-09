import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype
        """
        
        nodes_odd = queue.Queue()
        nodes_even = queue.Queue()
        if root:
            nodes_even.put(root)
        result = []
        while not nodes_even.empty() or not nodes_odd.empty():
            result_even = []
            while not nodes_even.empty():
                node = nodes_even.get()
                result_even.append(node)
            if result_even:
                result.append(result_even)
                for node in reversed(result_even):
                    if node.right is not None:
                        nodes_odd.put(node.right)
                    if node.left is not None:
                        nodes_odd.put(node.left)
            print("result_even:", list(map(lambda n: n.val, result_even)))
            
        
            result_odd = []
            while not nodes_odd.empty():
                node = nodes_odd.get()
                result_odd.append(node)
            if result_odd:
                result.append(result_odd)
                for node in reversed(result_odd):
                    if node.left is not None:
                        nodes_even.put(node.left)
                    if node.right is not None:
                        nodes_even.put(node.right)
            print("result_odd:", list(map(lambda n: n.val, result_odd)))
            
        return list(map(lambda outer: list(map(lambda inner: inner.val, outer)), result))
        
 
solution = Solution()

root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
node5 = TreeNode(4)
node6 = TreeNode(8)
node7 = TreeNode(6)
node8 = TreeNode(8)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
node1.left = node5
node1.right = node6
node5.right = node7
node6.left = node8

result = solution.zigzagLevelOrder(root)
print(result)