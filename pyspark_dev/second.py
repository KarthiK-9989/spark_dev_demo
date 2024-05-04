class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node

  def display(self):
    current = self.head
    while current is not None:
      print(current.data, end=" -> ")
      current = current.next
    print("null")

  def delete(self, data):
    if self.head is None:
      return

    # Handle deleting the head node
    if self.head.data == data:
      self.head = self.head.next
      return

    current = self.head
    prev = None
    while current is not None and current.next is not None:
      if current.next.data == data:
        prev.next = current.next.next
        return
      prev = current
      current = current.next

    # If loop completes without finding the element, it wasn't present
    print("Element not found in the list")

# Example usage
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Linked List:")
linked_list.display()

element_to_delete = 10
linked_list.delete(element_to_delete)

print(f"\nLinked List after deleting {element_to_delete}:")
linked_list.display()
