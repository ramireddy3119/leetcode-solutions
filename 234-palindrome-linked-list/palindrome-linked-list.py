# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        last = None
        while slow:
            nextNode = slow.next
            slow.next = last
            last = slow
            slow = nextNode

        left ,right = head,last
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next

        return True
        