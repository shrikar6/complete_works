def buy_and_sell_stock_once(prices):
    min_price_so_far = prices[0]
    max_profit_so_far = 0
    for i in range(len(prices)):
        if prices[i] < min_price_so_far:
            min_price_so_far = prices[i]
        max_profit_so_far = max(max_profit_so_far, prices[i] - min_price_so_far)
    return max_profit_so_far

print(buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))