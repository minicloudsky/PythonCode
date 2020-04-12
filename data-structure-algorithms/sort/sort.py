import random


def quicksort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums if i < pivot]
        greater = [i for i in nums if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def leftchild(i):
    return 2 * i + 1


def down(nums, n):
    child = None
    temp = None


if __name__ == '__main__':
    nums = [random.randint(-100, 100) for i in range(10)]
    # print(quicksort(nums))
    print(__file__)