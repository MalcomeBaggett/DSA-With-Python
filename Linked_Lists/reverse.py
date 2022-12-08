# Write a function, reverse_list, that takes in the head of a linked list as an argument.
# The function should reverse the order of the nodes in the linked list
# in-place and return the new head of the reversed linked list.


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def reverse_list_recursive(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)
