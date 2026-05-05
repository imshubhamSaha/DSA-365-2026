#  61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        # deep cloning linked List to avoid the manipulation of input data
        temp = ListNode()
        prev = temp
        t1 = head
        while t1 :
            prev.next = ListNode(t1.val)
            prev = prev.next
            t1 = t1.next
        temp = temp.next

        # variables for solving the problem
        total_nodes = 1
        curr = temp.next
        reverse = temp
        reverse.next = None

        # reverse the list
        while curr :
            next_node = curr.next
            curr.next = reverse
            reverse = curr
            curr = next_node
            total_nodes += 1

        #taking modulation to avoid out of scope rotation
        dup_k = (k % total_nodes)
        if not dup_k : 
            return head
        # reversing first portion by right position
        curr = reverse
        last_pos = curr
        prev = None
        while dup_k > 0 :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            dup_k -= 1
        
        
        new_head = prev
        prev = None
      
        while curr :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        last_pos.next = prev

        return new_head

