class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self) -> int:
        l = 0
        if self.head is None:
            return 0
        
        temp = self.head
        while temp is not None:
            l += 1
            temp = temp.next
        return l
    
    def search(self, data):
        if self.head is None:
            raise LookupError("LinkedList is empty")
        
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        
        return False
    
    def append(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp is not None:
            temp = temp.next
        
        temp.next = new_node
    
    def insert(self, position, data):
        pass
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "-> ", end="")
            temp= temp.next
        print(None)

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
    