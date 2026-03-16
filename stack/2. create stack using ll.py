"""
Implement a Stack using a Linked List, this stack has no fixed capacity and can grow dynamically until memory is available.
The Stack must support the following operations:

(i) push(x): Insert an element x at the top of the stack.
(ii) pop(): Remove the element from the top of the stack.
(iii) peek(): Return top element if not empty, else -1.
(iv) isEmpty(): Return true if the stack is empty else return false.
(v) size(): Return the number of elements currently in the stack.

There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call push(x)
2: Call pop()
3: Call peek()
4: Call isEmpty()
5: Call size()
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None
        self.count = 0 # just to have length of stack

    def push(self, x):
        new_node = Node(x)

        if self.top is None:
            self.top = new_node
            self.count += 1
            return
        
        new_node.next = self.top
        self.top = new_node
        self.count += 1


    def pop(self):
        if self.isEmpty():
            return -1
        
        ele = self.top.data

        self.top = self.top.next
        self.count -= 1

        return ele

    def peek(self):
        if self.isEmpty():
            return -1
        
        return self.top.data

    def isEmpty(self):
        if self.top is None:
            return True
        
        return False

    def size(self):
        temp = self.top
        l = 0
        while temp is not None:
            l += 1
            temp = temp.next
        
        return l
    
        # return self.count