class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        seter = set(nums)

        for num in nums:
            if num - 1 not in seter:
                leng = 1
                while num + leng in seter:
                    leng += 1

                res = max(res, leng)

        return res