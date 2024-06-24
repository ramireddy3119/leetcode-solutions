# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        def kthNode(head,k):
            temp = head
            count = 1
            while temp:
                if count == k: return temp
                count += 1
                temp = temp.next
            return temp
        tail = head 
        count = 1
        while tail.next:
            count += 1
            tail = tail.next
        if k%count == 0:
            return head
        k = k % count
        tail.next = head
        newNode = kthNode(head,count-k)
        head = newNode.next
        newNode.next = None
        return head