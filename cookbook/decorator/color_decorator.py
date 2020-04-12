def bold(func):
    print('------bold-----')

    def inner():
        print('---- bold decorator ---')
        return "<b>" + func() + "</b>"

    return inner


def italic(func):
    print('------italic----')

    def inner():
        print('---- italic decorator -----')
        return "<i>" + func() + "</i>"

    return inner


@bold
@italic
def foo():
    return "hello world"


if __name__ == '__main__':
    result = foo()
    print(result)
