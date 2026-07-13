class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        logest_map = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in logest_map:
                r = 1
                while num + r in logest_map:
                    r += 1
                res = max(res, r)
        return res