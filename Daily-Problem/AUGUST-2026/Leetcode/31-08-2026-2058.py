# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        node_pos = 2
        min_dist = float('inf')
        first_critical_point = last_critical_point = -1
        while curr.next :
            is_maxima = (curr.val > prev.val and curr.val > curr.next.val) 
            is_minima = (curr.val < prev.val and curr.val < curr.next.val)
            if is_maxima or is_minima :
                if first_critical_point == -1 :
                    first_critical_point = node_pos
                else :
                    min_dist = min(min_dist,node_pos - last_critical_point)
                last_critical_point = node_pos
            prev = curr
            curr = curr.next
            node_pos += 1

        if first_critical_point == -1 or first_critical_point == last_critical_point:
            return [-1,-1]
            
        max_dist = last_critical_point - first_critical_point
        return [min_dist , max_dist]
