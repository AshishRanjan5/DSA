class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        new_node = LinkedListNode(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def length(self) -> int:
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