def maxProfitBruteForce(prices=[7,1,5,3,6,4]):
    length = len(prices)
    maxProfit = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            profit = prices[j] - prices[i]
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit
def maxProfitDP(prices=[7,1,5,3,6,4]):
    minPrice = float('inf')
    maxProfit = 0
    for i in prices:
        if i < minPrice:
            minPrice = i
        elif i - minPrice > maxProfit:
            maxProfit = i - minPrice
    return maxProfit
print(maxProfitBruteForce())