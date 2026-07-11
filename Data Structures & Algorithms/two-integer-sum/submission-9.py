class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        res = []
        # for i in range(len(nums)):
        #     sum_map[i] = nums[i]

        for i in range(len(nums)):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if target - nums[i] in nums and i != j:
                    return [i, j] if j > i else [j, i]
        return []