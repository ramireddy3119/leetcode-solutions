# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            i+=1
            temp = temp.next
        return head
        