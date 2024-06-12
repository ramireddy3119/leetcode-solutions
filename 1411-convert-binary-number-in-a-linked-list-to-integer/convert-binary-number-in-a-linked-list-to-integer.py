# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        res = 0
        while temp is not None:
            res  = res*2+temp.val
            temp = temp.next
        return res
        