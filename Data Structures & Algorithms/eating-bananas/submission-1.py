class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            if total_hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
