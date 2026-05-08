class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        map_dic = {}

        for i in range(len(nums)):
            if target - nums[i] in map_dic:
                return [map_dic[target - nums[i]], i]
            map_dic[nums[i]] = i

