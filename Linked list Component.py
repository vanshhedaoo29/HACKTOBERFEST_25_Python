# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        # Convert nums to a set for O(1) lookups
        num_set = set(nums)
        count = 0
        curr = head

        # Traverse the linked list
        while curr:
            # If current node is in nums and
            # either next node is None or not in nums → end of a component
            if curr.val in num_set and (curr.next is None or curr.next.val not in num_set):
                count += 1
            curr = curr.next

        return count
