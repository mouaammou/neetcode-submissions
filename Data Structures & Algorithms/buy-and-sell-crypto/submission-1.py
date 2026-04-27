class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     min_price = prices[0]
    #     max_profit = 0

    #     for price in prices[1:]:
    #         profit = price - min_price
    #         max_profit = max(max_profit, profit)

    #         min_price = min(min_price, price)

    #     return max_profit

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                buy_price = prices[i]
                profit = prices[j] - buy_price
                max_profit = max(max_profit, profit)
        return (max_profit)