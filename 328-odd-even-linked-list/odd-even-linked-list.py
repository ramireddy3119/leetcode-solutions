# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        arr = []
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        
        temp = head.next
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            i+=1
            temp = temp.next
        return head

        