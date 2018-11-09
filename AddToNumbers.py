# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        root = None
        prev_node = None
        carry = 0
        while node1 is not None or node2 is not None:
            val1 = 0 if node1 is None else node1.val
            val2 = 0 if node2 is None else node2.val
            result = val1+val2+carry
            node = ListNode(result%10)
            carry = result//10
            if root is None:
                root = node
            if prev_node is not None:
                prev_node.next = node
            prev_node = node
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        if carry > 0:
            node = ListNode(carry)
            prev_node.next = node

        return root


number1 = ListNode(2)
number1.next = ListNode(4)
number1.next.next = ListNode(3)
number2 = ListNode(5)
number2.next = ListNode(6)
number2.next.next = ListNode(4)
number3 = ListNode(9)
number3.next = ListNode(9)
number3.next.next = ListNode(9)
number3.next.next.next = ListNode(9)

solution = Solution()

def printList(l):
    while(l!=None):
        print(l.val, ',')
        l = l.next

printList(solution.addTwoNumbers(number1, number3))
