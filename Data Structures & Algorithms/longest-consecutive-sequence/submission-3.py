class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        hash_set = set(nums)
        res = 0

        for i in range(len(nums)):
            cur = nums[i]
            len_cur = 0
            while cur in hash_set:
                cur += 1
                len_cur += 1
            res = max(res, len_cur)

        return res