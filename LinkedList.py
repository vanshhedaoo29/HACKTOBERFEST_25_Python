class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next           # move one step
        fast = fast.next.next      # move two steps

        if slow == fast:
            return True            # cycle detected

    return False                   # reached end -> no cycle
