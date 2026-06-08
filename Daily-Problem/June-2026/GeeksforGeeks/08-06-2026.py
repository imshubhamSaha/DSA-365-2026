# Delete Nodes with Greater on Right

'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    # reverse linked list
    def reverseList (self, head) :
        curr = head
        prev = None
        
        while curr :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
    
        return prev
        
    def compute(self,head):
        curr = head
        dup_head = Node(curr.data)
        prev = dup_head
        curr = curr.next
      
        while curr :
            prev.next = Node(curr.data)
            prev = prev.next
            curr = curr.next
            
        reverse_list = self.reverseList(dup_head)
        
        highest = reverse_list.data
        curr = reverse_list
        prev = curr
        curr = curr.next
        while curr :
            node_val = curr.data
            if node_val >= highest :
                highest = node_val
                prev.next = curr
                prev = curr
            curr = curr.next
        
        prev.next = None
        
        return self.reverseList(reverse_list)
        
