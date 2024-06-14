# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mpp = {}
        temp = head
        while temp:
            if temp in mpp:
                return True
            mpp[temp] = 1
            temp = temp.next
        return False