# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        temp = head
        while temp and temp.next:
            nextNode = temp.next 
            while nextNode and temp.val == nextNode.val:
                nextNode = nextNode.next
            temp.next = nextNode
            temp = temp.next
        return head
        