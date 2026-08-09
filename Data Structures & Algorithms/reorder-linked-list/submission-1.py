# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Input: head = [2,4,6,8]
slow ->2->4
fast->4->8->null
l2->8->6
l1->2

tmp 1->4
tmp2->6
l1->2->8->4->6

Output: [2,8,4,6]

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        prev = slow.next = None
        while l2!=None:
            nxt = l2.next   #8 
            l2.next = prev  #6   
            prev = l2       #6
            l2 = nxt        #8
        l1,l2 = head,prev
        while l2:
            tmp1,tmp2 = l1.next,l2.next
            l1.next = l2
            l2.next = tmp1
            l1,l2=tmp1,tmp2

