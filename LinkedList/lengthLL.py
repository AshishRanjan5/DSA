class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def lengthLL(self, head) -> int:
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next

        return length 

    
    def printLL(self, head) -> None:
        temp = head
        while temp is not None:
            print(temp.data)
            temp=temp.next


if __name__ == "__main__":
    n1 = LinkedListNode(10)
    n2 = n1.next = LinkedListNode(30)
    n3 = n2.next = LinkedListNode(20)

    LL = LinkedList()
    LL.printLL(n1)
    print(LL.lengthLL(n2))
