# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

def linked_list_values(head):
  values = []
  curr = head
  while curr is not None:
    values.append(curr.val)
    curr = curr.next
  return values