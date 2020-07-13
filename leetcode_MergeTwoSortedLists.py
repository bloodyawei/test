# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1 or not l2:
        #     return l1 or l2
        # l3_head = ListNode(0)
        # l3 = l3_head
        # while l1 or l2:
        #     if not l1:      #l1 done
        #         l3.next = l2
        #         break
        #     elif not l2:    #l2 done
        #         l3.next = l1
        #         break
        #     elif l1.val < l2.val:
        #         l3.next = l1
        #         l1 = l1.next
        #         l3 = l3.next
        #     else:
        #         l3.next = l2
        #         l2 = l2.next
        #         l3 = l3.next
        # return l3_head.next

        # if not l1 or not l2:
        #     return l1 or l2
        # head = cur = ListNode(0)
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # cur.next = l1 or l2
        # return head.next

        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2