def buy_and_sell_stock_twice(prices):
    second_buy_sell_max_profits = [0]*len(prices)
    max_so_far = prices[-1]
    for i in range(len(prices) - 1, -1, -1):
        max_so_far = max(max_so_far, prices[i])
        second_buy_sell_max_profits[i] = max_so_far - prices[i]
    max_profit = 0
    min_so_far = prices[0]
    for i in range(len(prices) - 1):
        min_so_far = min(min_so_far, prices[i])
        max_profit = max(max_profit, prices[i] - min_so_far + second_buy_sell_max_profits[i+1])
    return max_profit

def buy_and_sell_stock_twice_v2(prices):
    max_profit1 = 0
    min_so_far1 = prices[0]
    max_profit2 = 0
    min_so_far2 = prices[0]
    for i in range(len(prices)):
        min_so_far1 = min(min_so_far1, prices[i])
        max_profit1 = max(max_profit1, prices[i] - min_so_far1)
        min_so_far2 = min(min_so_far2, prices[i] - max_profit1)
        max_profit2 = max(max_profit2, prices[i] - min_so_far2)
    return max_profit2

print(buy_and_sell_stock_twice_v2([12,11,13,9,12,8,14,13,15]))