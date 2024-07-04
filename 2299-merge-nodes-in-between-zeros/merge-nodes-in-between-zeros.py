# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dummyNode = ListNode(-1)
        res = dummyNode
        while temp:
            if temp.val == 0:
                temp = temp.next
                continue
            sum = 0
            while temp and temp.val !=0:
                sum += temp.val
                temp = temp.next
            res.next=ListNode(sum)
            res = res.next
        return dummyNode.next



        