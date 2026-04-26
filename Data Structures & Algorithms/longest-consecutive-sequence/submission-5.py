class Solution:

    # brute force
    # def longestConsecutive(self, nums: List[int]) -> int:
       
    #     hash_set = set(nums)
    #     res = 0

    #     for i in range(len(nums)):
    #         cur = nums[i]
    #         len_cur = 0
    #         while cur in hash_set:
    #             cur += 1
    #             len_cur += 1
    #         res = max(res, len_cur)

    #     return res

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     nums.sort()
    #     n = len(nums)
    #     cur, len_cur = nums[0], 0
    #     res = 0
    #     i = 0
    #     while i < n:
    #         if nums[i] != cur:
    #             cur = nums[i]
    #             len_cur = 0
    #         while i < n and cur == nums[i]:
    #             i += 1
    #         cur += 1
    #         len_cur += 1
    #         res = max(res, len_cur)

    #     return res

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hash_set = set(nums)
        res = 0
        for num in hash_set:
            if (num - 1) not in hash_set:
                seq_len = 1
                while (num + seq_len) in hash_set:
                    seq_len += 1
                res = max(res, seq_len)
        return res