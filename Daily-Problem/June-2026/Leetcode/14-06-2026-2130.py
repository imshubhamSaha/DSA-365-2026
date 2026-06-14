# 2130. Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None 

        while fast and fast.next :
            fast = fast.next.next
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        result = 0

        while slow and prev :
            result = max(result, (slow.val + prev.val))
            slow = slow.next
            prev = prev.next

        return result
