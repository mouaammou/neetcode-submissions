class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(len(nums)):
            j = 0
            res = 1
            while j < len(nums):
                if j != i:
                    res *= nums[j]
                    # print(nums[j])
                j+= 1
            # print("ss")
            output.append(res)
        # print(output)
        return output