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
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
    
    def insert(self, data, position):
        if position == 0:
            return
        new_node = LinkedListNode(data)
        temp = self.head
        current_position = 0
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        while current_position < position-1:
            temp = temp.next
            current_position += 1
        
        new_node.next = temp.next
        temp.next = new_node

    def removeEveryKthNode(self, K):
        
        if self.head is None or K <= 0:
            return self.head

        curr = self.head
        prev = None

        count = 0

        while curr is not None:
            count += 1

            
            if count % K == 0:
            
                
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            else:
                prev = curr

            curr = curr.next

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
    ll.insert(40, 2)
    ll.insert(70, 0)
    ll.insert(50, 4)
    ll.display()
    ll.removeEveryKthNode(2)
    ll.display()