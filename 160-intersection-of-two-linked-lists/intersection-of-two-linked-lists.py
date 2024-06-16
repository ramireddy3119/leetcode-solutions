# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        mpp = {}
        temp = headA
        while temp:
            mpp[temp]=1
            temp = temp.next
        temp = headB
        while temp:
            if temp in mpp:
                return temp
            temp = temp.next
        return None
        