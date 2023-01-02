class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insertion(self,data):
        new_node = Node(data)
        if new_node.data < self.data:
            if self.left != None:
                self.left.insertion(data)
            else:
                self.left = new_node
        elif new_node.data > self.data:
            if self.right != None:
                self.right.insertion(data)
            else:
                self.right = new_node
    def preorderTraversal(self):
        ls = []
        ls.append(self.data)
        if self.right != None:
            ls = ls + self.right.preorderTraversal()
        if self.left != None:
            ls = ls + self.left.preorderTraversal()
        return ls

    def search(self,value):
        if self.data == value:
            return self
        elif self.left.data == value:
            return self.left
        elif self.right.data == value:
            return self.right
        else:
            return 'no such value in tree'


root = Node(10)
root.insertion(1)
root.insertion(14)
root.insertion(16)
root.insertion(5)
root.insertion(19)
root.insertion(2)
root.insertion(9)
root.insertion(54)
root.insertion(3)
root.insertion(12)
root.insertion(6)
root.insertion(8)
print(root.preorderTraversal())
print(root.search(17))