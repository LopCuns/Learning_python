# El stack es una estructura de datos que puede albergar diferentes elementos de manera que se recuperan como en una pila,solo el ultimo en entrar.
# Sigue así el concepto de LIFO , Last In First Out o último dentro primero fuera
# https://www.youtube.com/watch?v=I5lq6sCuABE&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY&index=4

class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self,value):
        self.items.append(value)
    def peek(self):
        return self.items[-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)



myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.size())
print(myStack.isEmpty())
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())