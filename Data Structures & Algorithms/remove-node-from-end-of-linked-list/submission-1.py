# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        linkLen = 0
        curr = head
        while curr:
            linkLen +=1
            curr = curr.next
        if n == linkLen:
            return head.next
        curr = head
        steps = linkLen - n - 1
        for _ in range(steps): ## goes up to the node before the one we want to remove
            curr = curr.next
        curr.next = curr.next.next
        return head