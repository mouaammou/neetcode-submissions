class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {i: None for i in nums}

        for i in range (len(nums)):
            if target - nums[i] in hash_map:
                if hash_map[nums[i]] is None:
                    hash_map[target - nums[i]] = i
                    print("ues", hash_map)
                else :
                    return [hash_map[nums[i]], i]      
        return [-1, -1]