def deco(func):
    def wrapper():
        print(func.__name__, 'func start')
        func()
        print(func.__name__, 'func end')
    return wrapper

@deco
def hello():
    print('hello')

@deco
def world():
    print('world')


if __name__ == '__main__':
    hello()
    print()
    world()

    # temp_func = deco(hello)
    # temp_func()
