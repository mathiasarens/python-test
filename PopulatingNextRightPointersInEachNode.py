import queue

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        depth = {}
        node_queue = queue.Queue()
        node_queue.put(root)
        depth[root] = 0
        prev_node = None
        while node_queue.empty() is False:
            node = node_queue.get()
            if node.left is not None:
                node_queue.put(node.left)
                depth[node.left] = depth[node] + 1
            if node.right is not None:
                node_queue.put(node.right)
                depth[node.right] = depth[node] + 1

            if prev_node is not None:
                if depth[prev_node] == depth[node]:
                    prev_node.next = node

            prev_node = node

root = TreeLinkNode(0)
root.left = TreeLinkNode(1)
root.right = TreeLinkNode(2)

solution = Solution()
solution.connect(root)
print(root)
