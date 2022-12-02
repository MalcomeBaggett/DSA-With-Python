# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
# The function should return the total sum of all values in the linked list.


def sum_list(head):
    sum = 0
    while head is not None:
        sum += head.val
        head = head.next
    return sum
