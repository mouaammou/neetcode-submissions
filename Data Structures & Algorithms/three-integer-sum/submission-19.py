class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                som = nums[i] + nums[left] + nums[right]

                if som == 0:
                    if (nums[i] , nums[left] , nums[right]) not in res:
                        res.add((nums[i] , nums[left] , nums[right]))
                    left += 1
                elif som > 0:
                    right -= 1
                else: 
                    left += 1

        res = list(res)
        return res