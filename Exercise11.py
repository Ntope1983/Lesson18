class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
         if self.head is None:
             return True
         else:
             return False

    def insert_start(self,data):
        Node_new=Node(data,self.head)
        self.head=Node_new