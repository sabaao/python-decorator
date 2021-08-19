class decoratorClass(object):
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self,f):
        def wrapper(*args,**kwargs):
            print(f"do somthing before calling function {f.__name__} , with {self.p1}")
            f(*args,**kwargs)
            print(f"do somthing after calling function{f.__name__} , with {self.p2}")
        return wrapper

@decoratorClass('parameter1','parameter2')
def myFunc():
    print('main')

if __name__=='__main__':
    myFunc()
    # do somthing before calling function myFunc , with parameter1
    # main
    # do somthing after calling functionmyFunc , with parameter2