from functools import wraps

def decorate(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        print(f'do something before calling function {f.__name__}')
        f(*args,**kwargs)
        print(f'do somethine after calling function {f.__name__}')
    return wrapper

@decorate
def myFunc():
    print('main')

if __name__=='__main__':
    myFunc()
    # do something before calling function myFunc
    # main
    # do somethine after calling function myFunc