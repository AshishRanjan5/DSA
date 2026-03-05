class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DoublyLinkedListNode(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def length(self):
        if self.head is None:
            return 0
        l = 0
        temp = self.head
        while temp is not None:
            l += 1
            temp = temp.next
        
        return l
    
    def display(self):

        temp = self.head

        if temp is None:
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("\n")
    
    def displayReverse(self):
        temp = self.head

        if temp is None:
            return

        while temp.next is not None:
            temp = temp.next
        
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.prev
        
        print("\n")
    
    def insert(self, data, index):
        if self.head is None and index > 0:
            raise IndexError("Index out of bound")
        
        new_node = DoublyLinkedListNode(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr_index = 0
        temp = self.head

        while temp is not None and curr_index < index-1:
            temp = temp.next
            curr_index += 1
        
        if temp is None:
            raise IndexError("Index out of bounds")

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node
    
    def delete(self, index):
        if self.head is None and index > 0:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        
        temp = self.head

        curr_index = 0

        while temp is not None and curr_index < index - 1:
            temp = temp.next
            curr_index += 1
        
        if temp is None:
            raise IndexError("Index out of bounds")

        node_to_delete = temp.next

        temp.next = node_to_delete.next

        if node_to_delete.next is not None:
            node_to_delete.next.prev = temp


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(30)
    dll.append(20)
    dll.append(50)

    dll.display()
    dll.displayReverse()
    print("length of DLL:", dll.length())
    dll.insert(40, 3)
    dll.display()
    dll.delete(3)
    dll.display()
