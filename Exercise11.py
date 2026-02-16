class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
        return not isinstance(self.head, Node)

    def insert_start(self, data):
        self.head = Node(data)

    def insert_after(self, node, data):
        flag = self.head
        while not flag is None:
            if flag is node:
                temp = node
                flag = Node(data)
                Node.next = temp
                break
            else:
                flag = flag.next
        print("Δεν βρέθηκε το  Node ")


list1 = LinkedList()
list1.insert_start(10)
list1.insert_after(10,20)

