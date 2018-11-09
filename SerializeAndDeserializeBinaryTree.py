# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.preorder_serialize(root, "")[:-1]

    def preorder_serialize(self, node, encodedString):
        if node:
            encodedString = encodedString + str(node.val) + ','
            encodedString = self.preorder_serialize(node.left, encodedString)
            encodedString = self.preorder_serialize(node.right, encodedString)
        else:
            encodedString = encodedString + 'X,'
        return encodedString

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        value_list = data.split(',')
        if (len(value_list) < 1):
            return None
        root = None
        root_value = value_list.pop(0)
        if root_value != 'X':
            root = TreeNode(root_value)
            self.preorder_deserialize(value_list, root)
        return root
        
    def preorder_deserialize(self, value_list, node):
        if value_list:
            # left
            node_value_left = value_list.pop(0)
            if node_value_left != 'X':
                node_left = TreeNode(node_value_left)
                node.left = node_left
                self.preorder_deserialize(value_list, node_left)
            # right
            node_value_right = value_list.pop(0)
            if node_value_right != 'X':
                node_right = TreeNode(node_value_right)
                node.right = node_right
                self.preorder_deserialize(value_list, node_right)

            


# Your Codec object will be instantiated and called as such:

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
# node1.right = node2
# node2.right= node3
# node3.right = node4
# node4.right = node5

node1.left = node2
node1.right= node3
node3.left = node4
node3.right = node5

codec = Codec()
root = codec.deserialize(codec.serialize(None))
root