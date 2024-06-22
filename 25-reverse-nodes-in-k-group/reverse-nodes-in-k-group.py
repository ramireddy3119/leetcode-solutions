# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kthElement(head,k):
            k -= 1
            temp = head
            while temp and k > 0:
                temp = temp.next
                k -= 1
            return temp
        def reverse(head):
            temp = head
            prev = None
            while temp:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev
        temp = head
        back = None
        while temp:
            kthNode = kthElement(temp,k)
            if kthNode == None:
                if back:
                    back.next = temp
                break
            nextNode = kthNode.next
            kthNode.next = None
            reverse(temp)
            if temp == head:
                head = kthNode
            else:
                back.next = kthNode
            back = temp
            temp = nextNode
        return head
                
        