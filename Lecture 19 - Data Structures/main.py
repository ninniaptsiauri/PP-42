# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
        
#         else:
#             last_node = self.head

#             while last_node.next is not None:
#                 last_node = last_node.next

#             last_node.next = new_node


#     def insert(self, data, index):
#         new_node = Node(data)

#         if index == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
        
#         current_node = self.head
#         current_index = 0

#         while current_node.next and current_index < index - 1:
#             current_node = current_node.next
#             current_index += 1

#         new_node.next = current_node.next
#         current_node.next = new_node


#     def delete(self, index):
#         if index == 0:
#             self.head = self.head.next
#             return
        
#         current_node = self.head
#         current_index = 0

#         while current_node.next and current_index < index - 1:
#             current_node = current_node.next
#             current_index += 1

#         if current_node.next:
#             current_node.next = current_node.next.next


#     def display(self):
#         current_node = self.head

#         while current_node is not None:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
        
#         print()


# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.display()

# linked_list.insert(9, 1)
# linked_list.display()

# linked_list.delete(1)
# linked_list.display()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self.length = 0

    def empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def top(self):
        if not self.empty():
            return self.top_node.data
        
        else:
            raise IndexError("Stack is empty")
        
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        
        else:
            raise IndexError("Stack is empty")
        

stack = Stack()
print("Length: ", stack.length)
stack.push(1)
stack.push(2)
stack.push(3)
print("Length: ", stack.length)
print(stack.top())

print(stack.pop())
print("Length: ", stack.length)


from collections import deque

deque_info = deque([1, 2, 3, 4, 5, 1, 5, 4])
print(deque_info)

print(deque_info.count(2))
print(deque_info.count(4))

deque_info.append(11)
print(deque_info)

deque_info.appendleft(22)
print(deque_info)

deque_info.pop()
print(deque_info)

deque_info.popleft()
print(deque_info)


from queue import Queue

queue_info = Queue(maxsize=3)
queue_info.put(1)
queue_info.put(2)
queue_info.put(3)
print(queue_info.full())
print(queue_info.empty())
print("Size", queue_info.qsize())
# queue_info.put_nowait(4)
queue_info.get()
queue_info.put(4)

print(queue_info.get())
print(queue_info.get())
print(queue_info.get())
print(queue_info.empty())
# print(queue_info.get_nowait())

