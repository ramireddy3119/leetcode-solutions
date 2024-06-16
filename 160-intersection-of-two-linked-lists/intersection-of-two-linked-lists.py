# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        temp1 = headA
        temp2 = headB
        while temp1 != temp2:
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA
        return temp1
            
                
        