from functools import wraps

def decorate(p1,p2):
    def outer_warpper(f):
        @wraps(f)
        def wrapper(*args,**kwargs):
            print(f'do something before calling function {f.__name__} with {p1}')
            f(*args,**kwargs)
            print(f'do something after calling function {f.__name__} with {p2}')
        return wrapper
    return outer_warpper

@decorate('p1','p2')
def myFunc():
    print('main')

if __name__ == '__main__':
    myFunc()
    # do something before calling function myFunc with p1
    # main
    # do something after calling function myFunc with p2