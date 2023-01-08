import functools

# function decorators

def repeatDecorator(num_reps):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            for _ in range(num_reps):
                fn(*args,**kwargs)
        return wrapper
    return deco



@repeatDecorator(4)
def sayHi(name):
    print(f'hello { name } ')

sayHi('jlop')



# Class decorators
class controlSayHola:
    def __init__(self,fn):
        self.fn = fn
        self.times = 0
    def __call__(self,*args,**kwargs):
        self.times +=1
        print(self.times)
        self.fn(*args,**kwargs)

@controlSayHola
def sayHola(name):
    print(f'hola { name } ')

sayHola('jlop')
sayHola('jlop')
sayHola('jlop')
sayHola('jlop')
sayHola('jlop')
sayHola('jlop')
