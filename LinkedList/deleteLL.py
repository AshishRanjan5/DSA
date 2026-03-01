class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self)-> int:
        temp = self.head
        l = 0
        while temp is not None:
            l += 1
            temp = temp.next
        return l
    
    def search(self, data) -> bool:
        if self.head is None:
            return False
        
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        
        return False

    def append(self, data) -> None:
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def insert(self, data, position) -> None:
        new_node = LinkedListNode(data)
        if position < 0:
            raise IndexError("Index cannot be negative")

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_index = 0
        temp = self.head

        while temp is not None and current_index<position-1:
            current_index += 1
            temp = temp.next

        if temp is None:
            raise IndexError("Index out of bound")

        new_node.next = temp.next
        temp.next = new_node
    
    def delete(self, position):
        if position < 0:
            raise IndexError("Index cannot be negative")
        if position == 0:
            self.head = self.head.next
            return
        
        temp = self.head
        current_index = 0
        while temp is not None and current_index < position-1:
            temp = temp.next
            current_index += 1
        
        if temp is None:
            raise IndexError("Index out of bound")
        
        temp.next = temp.next.next

    def display(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(30)
    ll.append(20)

    ll.display()
    print(ll.length())
    print(ll.search(30))
    ll.insert(40, 2) # insertion somewhere in the middle
    ll.insert(70, 0) # insertion in starting index
    ll.insert(50, 4) # insertion at the end of the index
    print("Before delete")
    ll.display()
    ll.delete(3)
    print("After delete")
    ll.display()
    