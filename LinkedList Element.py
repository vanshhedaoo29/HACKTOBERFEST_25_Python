class Solution(object):
    def removeElements(self, head, val):
        # Create a dummy node that points to head
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Skip the node
            else:
                current = current.next
        
        # Return the updated list, skipping dummy node
        return dummy.next
