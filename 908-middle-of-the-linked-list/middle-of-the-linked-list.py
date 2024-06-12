# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def calculate_length(head):
            temp = head
            count = 0
            while temp:
                temp = temp.next
                count += 1
            return count
        count = 0
        temp = head
        length = calculate_length(head)
        half = 0
        if length%2 != 0:
            half = (length//2)
        else:
            half = length//2
        while count != half:
            temp = temp.next
            count += 1
        return temp

        
        