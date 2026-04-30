class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        for right in range(k, len(nums) + 1):
            window = nums[left: right]
            
            window.sort()
            res.append(max(window))
            left += 1
        return res
        