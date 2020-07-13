# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # if head is None:
        #     return False
        # fast = head.next
        # slow = head
        # while slow is not None and fast is not None and fast.next is not None:
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     fast = fast.next.next
        # return False
        visited = []
        curr = head
        while curr and curr.next:
            if curr in visited:
                return True
            else:
                visited.append(curr)
                curr = curr.next
        return False