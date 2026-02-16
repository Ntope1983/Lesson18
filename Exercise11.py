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
        self.head = Node(data, self.head)

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
        flag = self.head
        result = ""
        while flag is not None:
            result += "-" + str(flag)
            flag = flag.next
        return result

list1 = LinkedList()

list1.insert_start(10)
node_x = list1.head

list1.insert_after(node_x, 20)
node_y = list1.head.next

list1.insert_after(node_y, 30)
list1.insert_after(node_x, 40)

print(f"H λίστα πριν {list1}")

list_s = list1.delete_after(node_x)

print(f"H λίστα μετά {list1}")
print("Τα nodes που αφαιρέθηκαν:")
for nod in list_s:
    print(str(nod))
