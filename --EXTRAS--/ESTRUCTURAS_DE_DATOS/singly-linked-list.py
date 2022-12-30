# https://www.youtube.com/watch?v=odW9FU8jPRQ&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY&index=3

class Node():
    def __init__(self,value,next):
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self,value):
        new_node = Node(value,self.head)
        self.head = new_node
        self.tail = (new_node,self.tail)[self.tail == None]

    def append(self,value):
        new_node = Node(value,None)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            self.head = new_node
            self.tail = new_node
    def insertAfter(self,value,nodeValue):
        prev_node = self.find(nodeValue)
        if prev_node != None:
            new_node = Node(value,prev_node.next) 
            prev_node.next = new_node
        else:
            return 'previous node does not exist'
        


    def find(self,value):
        current = self.head
        while not(current.value == value):
            current = current.next
            if(current == None):
                return 'node not found'
        else:
            return current

    def traverse(self,do):
        current = self.head
        while current != None:
            do(current.value)
            current = current.next

    def deleteHead(self):

        if not(self.head):
            return
        elif self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        
    def toList(self):
        list = []
        self.traverse(list.append)
        return list



my_linked_list = LinkedList()

my_linked_list.append('one')
my_linked_list.append('True')
my_linked_list.append('3')
my_linked_list.append('four')
my_linked_list.traverse(print)

print(my_linked_list.find('3').value)

my_linked_list.deleteHead()

my_linked_list.traverse(print)

print(my_linked_list.toList())

my_linked_list.insertAfter(5,'four')
my_linked_list.traverse(print)