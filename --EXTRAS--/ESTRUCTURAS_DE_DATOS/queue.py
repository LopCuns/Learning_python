# Las Queues funcionan como los Stacks con la diferencia de que funcionan según el principio FIFO, First In First Out
# https://www.youtube.com/watch?v=mDCi1lXd9hc&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY&index=5

class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self,value):
        self.items.append(value)
    
    def peek(self):
        return self.items[0]

    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

myQueue = Queue()
print(myQueue.isEmpty())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.size())
print(myQueue.peek())