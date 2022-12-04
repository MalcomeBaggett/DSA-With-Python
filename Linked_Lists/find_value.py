# Write a function, linked_list_find, that takes in the head of a linked list and a target value.
# The function should return a boolean indicating whether or not the linked list contains the target.


def linked_list_find(head, target):
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False
