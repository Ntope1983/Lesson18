class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Check if list is empty
    def empty(self):
        return self.head is None

    # Insert at beginning
    def insert_start(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    # Insert after a specific node (identity-based)
    def insert_after(self, node, data):
        flag = self.head
        while flag is not None:
            if flag is node:
                new_node = Node(data, flag.next)
                flag.next = new_node
                return
            flag = flag.next
        print("Δεν βρέθηκε το Node")

    # Remove first node
    def delete_start(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        return removed

    # Remove everything after a node and return removed nodes
    def delete_after(self, node):
        flag = self.head
        removed_nodes = []

        while flag is not None:
            if flag is node:
                current = flag.next
                while current is not None:
                    removed_nodes.append(current)
                    current = current.next
                flag.next = None
                return removed_nodes
            flag = flag.next

        print("Δεν βρέθηκε το Node")
        return []

    def __str__(self):
        nodes = []
        flag = self.head
        while flag:
            nodes.append(str(flag.data))
            flag = flag.next
        return "-" + "-".join(nodes) if nodes else ""


class OrderedList(LinkedList):
    def __init__(self):
        # Initialize the ordered list by calling parent constructor
        super().__init__()

    def insert(self, data):
        """
        Insert a new value while maintaining ascending order.

        Cases:
        1. If list is empty → insert at start.
        2. If new value is smaller than or equal to head → insert at start.
        3. Otherwise → traverse until correct position is found,
           then insert after the appropriate node.
        """

        if self.empty():  # Case 1: empty list
            self.insert_start(data)

        elif self.head.data >= data:  # Case 2: insert before head
            self.insert_start(data)

        else:
            # Case 3: find correct insertion position
            current = self.head

            # Move forward while next node exists
            # and next node's value is still smaller than data
            while current.next is not None and current.next.data < data:
                current = current.next

            # Insert after the last smaller element
            self.insert_after(current, data)

    def delete(self, data):
        """
        Delete the first occurrence of 'data'.

        Returns:
        - True if deletion was successful
        - False if data was not found or list is empty
        """

        # Case 1: empty list
        if self.head is None:
            return False

        current = self.head

        # Case 2: value is at head
        if current.data == data:
            self.head = current.next
            return True

        # Case 3: search for value in the rest of the list
        while current.next is not None:

            # If next node contains the target value,
            # bypass it (remove it from list)
            if current.next.data == data:
                current.next = current.next.next
                return True

            current = current.next

        # Value not found
        return False



x = OrderedList()
x.insert(5)
x.insert(4)
x.insert(4)
x.insert(150)
x.insert(1)
x.delete(150)
print(x)
