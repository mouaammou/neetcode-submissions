class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(len(nums)):
            j = 0
            res = 1
            while j < len(nums):
                if j != i:
                    res *= nums[j]
                j+= 1
            output.append(res)
        return output

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     output = [1] * n

    #     # left pass
    #     left = 1
    #     for i in range(n):
    #         output[i] = left
    #         left *= nums[i]

    #     # right pass
    #     right = 1
    #     for i in range(n-1, -1, -1):
    #         output[i] *= right
    #         right *= nums[i]

    #     return output