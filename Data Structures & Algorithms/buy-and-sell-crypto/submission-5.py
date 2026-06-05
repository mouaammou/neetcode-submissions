class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        res = 0
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])

        return res