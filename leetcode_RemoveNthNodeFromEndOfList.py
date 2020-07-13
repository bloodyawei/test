# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = head
        num_nodes = 0
        while tmp is not None:
            tmp = tmp.next
            num_nodes += 1
        k = num_nodes - n

        prev = None
        ptr = head
        while k != 0:
            prev = ptr
            ptr = ptr.next
            k -= 1

        if prev is None:
            return head.next
        else:
            prev.next = ptr.next
            ptr.next = None
            return head