def move(nums):
    temp = nums[0]
    list = [i for i in nums[1:]]
    list.append(temp)
    return list


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


if __name__ == '__main__':
# list = [0, 1, 2, 3, 4, 5, 6]
# print(move(list))
# d = {key: value for (key, value) in [{'1': 1, '2': 2}]}
# print(d)
