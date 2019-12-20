def maxProfit(prices=[1,2,3,4,5]):
    maxProfit = 0
    for i, v in enumerate(prices):
        if i == 0:
            continue
        if prices[i] > prices[i - 1]:
            maxProfit += prices[i] - prices[i - 1]
    return maxProfit
print(maxProfit())