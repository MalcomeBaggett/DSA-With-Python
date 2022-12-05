# Write a function, get_node_value, that takes in the head of a linked list and an index.
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.


def get_node_value(head, index):
    count = 0
    curr = head

    while curr is not None:
        if count == index:
            if curr is not None:
                return curr.val
            else:
                return None
        curr = curr.next
        count += 1
