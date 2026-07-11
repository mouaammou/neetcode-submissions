class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i in range(len(nums)):
            sum_map[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in sum_map:
                j = sum_map[target - nums[i]]
                if i != j:
                    return [i, j]
        return []