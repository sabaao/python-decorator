class decoratorClass(object):
    def __init__(self, f):
        self.f = f

    def __call__(self,*args, **kwargs):
        print(f"do somthing before calling function {self.f.__name__}")
        self.f(*args,**kwargs)
        print(f"do somthing after calling function{self.f.__name__}")

@decoratorClass
def myFunc():
    print('main')

if __name__=='__main__':
    myFunc()
    # do somthing before calling function myFunc
    # main
    # do somthing after calling functionmyFunc