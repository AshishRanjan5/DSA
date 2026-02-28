class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def lengthLL(self) -> int:
        temp = self.head
        length = 0

        while temp is not None:
            length += 1
            temp = temp.next
        
        return length
    
    def appendLL(self, data) -> None:
        new_node = LinkedListNode(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node

    
    def printLL(self) -> None:
        temp = self.head
        
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    ll = LinkedList()

    ll.appendLL(10)
    ll.appendLL(30)
    ll.appendLL(20)

    ll.printLL()

    
