# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # cur = head
        # while cur is not None:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        # return prev
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head