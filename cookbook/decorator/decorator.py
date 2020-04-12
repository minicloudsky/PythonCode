def outer(func):
    def inner():
        print('----inner---')
        func()

    return inner


def origin():
    print('----origin-----')


@outer
def foo():
    print('----foo---')


@outer
def bar():
    print('----bar----')


if __name__ == '__main__':
    foo()
    origin = outer(origin)
    origin()
