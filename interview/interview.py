s = """
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
"""
# 每一行的三个数字都是三角形的三条边，
# 请写程序判断满足条件的三角形(两边之和大于第三边)的个数


def solve(input):
    triangle_datas = input.split('\n')
    triangle_datas = [triangle_data for triangle_data in triangle_datas]


def test():
    s1 = """
    1 5 6
    2 6 8
    3 4 5
    1 2 4
    6 8 12
    """
    assert solve(s1) == 2


test()
