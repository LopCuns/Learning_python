class Node():
    def __init__(self,value,prev,next):
        self.value = value
        self.prev = prev
        self.next = next


class DLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self,value):
        new_node = Node(value,None,self.head)
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node
        self.tail = (new_node,self.tail)[self.tail == None]
    def append(self,value):
        new_node = Node(value,self.tail,None)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        
    def insertAfter(self,value,node):
        if node == None or type(node) != Node:
            return
        else:
            new_node = Node(value,node,node.next)
            node.next = new_node
            if new_node.next != None:
                new_node.next.prev = new_node
    def find(self,nodeValue):
        current = self.head
        while current.value != nodeValue:
            current = current.next
            if current == None:
                return 'node not found'            
        else:
            return current

    def traverse(self,do):
        current = self.head
        while current != None:
            do(current.value)
            current = current.next

    def deleteHead(self):
        if self.head == None:
            return
        elif self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
    def toList(self):
        list = []
        self.traverse(list.append)
        return list

        
my_linked_list = DLinkedList()

my_linked_list.append('one')
my_linked_list.append(True)
my_linked_list.append(3)
my_linked_list.append('four')
my_linked_list.traverse(print)
my_linked_list.deleteHead()
my_linked_list.insertAfter(5,my_linked_list.find(True))
print(my_linked_list.find(2))
print(my_linked_list.toList())
