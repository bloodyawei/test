# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        head_ = head
        node_val = []
        while head_:
            node_val.append(head_.val)
            head_ = head_.next
        for i in range(len(node_val)//2):
            if node_val[i] != node_val[len(node_val)-i-1]:
                return False
        return True

        # node_val.reverse()
        # for val in node_val:
        #     if val != head.val:
        #         return False
        #     else:
        #         head = head.next
        # return True