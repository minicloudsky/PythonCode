# 股票每日价格
S = [10, 4, 8, 7, 9, 6, 2, 5, 3]
maxProfit = 0
buyDate = 0
sellDate = 0
# 遍历所有组合，找出收益最高的买入和卖出时机
for start in range(len(S) - 1):
    for end in range(start, len(S)):
        if S[end] - S[start] > maxProfit:
            maxProfit = S[end] - S[start]
            buyDate = start + 1
            sellDate = end + 1
print({'buy': buyDate, 'sell': sellDate, 'maxProfit': maxProfit})
