class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            my_map[nums[i]] = i

        res = []
        for i in range(len(nums)):
            if target - nums[i] in my_map and my_map[target - nums[i]] != i:
                res.append(i)
                res.append(my_map[target - nums[i]])
                if len(res) == 2:
                    return res
        return res