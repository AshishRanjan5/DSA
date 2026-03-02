class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = LinkedListNode(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def length(self) -> int:
        if self.head is None:
            return 0
        l = 0
        temp = self.head
        while temp is not None:
            l += 1
            temp = temp.next
        
        return l
    
    def findNthfromEnd(self, N):
        l = self.length()
        if l < N:
            raise IndexError("Index out of bound")
        
        slow = self.head
        fast = self.head

        while N > 0:
            fast = fast.next
            N -= 1
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow.data
    
    def display(self) -> None:
        temp = self.head

        while temp is not None:
            print(temp.data , "-> ", end= "")
            temp = temp.next
        print(None)
    
if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(30)
    ll.append(20)
    ll.append(40)
    ll.append(60)
    ll.append(50)

    ll.display()
    print("\n")
    print(ll.findNthfromEnd(3))
