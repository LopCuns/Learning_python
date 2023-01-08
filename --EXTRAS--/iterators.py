list = [1,2,3,4,5,6]
list_iter = iter(list)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))


class Test():
    def __init__(self,limit):
        self.limit = limit
    
    def __iter__(self):
        self.x = 10
        return self
    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration

        self.x = x + 1

        return x


for i in Test(14):
    print(i)