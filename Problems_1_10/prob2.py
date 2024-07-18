# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Dummy node to simplify code and avoid special cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists
        while l1 or l2:
            # Get values or 0 if the list is already fully traversed
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            
            # Create a new node with the sum's unit place value
            current.next = ListNode(sum_val % 10)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they are not None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there's any carry left, create a new node with the carry value
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the next of dummy_head as the result list head
        return dummy_head.next
def print_linked_list(node):
    """ Helper function to print linked list """
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Creating linked list for l1 = [2, 4, 3]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Creating linked list for l2 = [5, 6, 4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Initialize the solution
solution = Solution()

# Adding the two numbers
result = solution.addTwoNumbers(l1, l2)

# Print the result
print_linked_list(result)