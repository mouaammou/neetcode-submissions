class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n - 1
        res = 0
        while left < right:
            
            height = min(heights[left], heights[right])
            width = right - left

            res = max(res, width * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res