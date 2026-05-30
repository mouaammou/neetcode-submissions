class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       
        res = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                res = max(res, prices[right] - prices[left])
            else:
                left = right

        return res