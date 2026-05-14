class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:

    #     output = []
    #     for i in range(len(nums)):
    #         j = 0
    #         res = 1
    #         while j < len(nums):
    #             if j != i:
    #                 res *= nums[j]
    #             j+= 1
    #         output.append(res)
    #     return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # left pass
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # right pass
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     left = [0] * n
    #     right = [0] * n
    #     res = [0] * n

    #     left[0] = 1
    #     for i in range(1, n):
    #         left[i] = nums[i - 1] * left[i - 1]
        
    #     right[n - 1] = 1
    #     for i in range(n - 2, -1 , -1):
    #         right[i] = right[i + 1] * nums[i + 1]

    #     for i in range(n):
    #         res[i] = left[i] * right[i]

        
    #     return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     ziro_count = 0

    #     res = [0] * n

    #     max_prod = 1

    #     for i in range(n):
    #         if nums[i] == 0:
    #             ziro_count += 1
    #             continue
    #         max_prod *= nums[i]

    #     if ziro_count > 1:
    #         return res

    #     for i in range(n):
    #         if ziro_count:
    #             if nums[i] == 0:
    #                 res[i] = max_prod
    #         else:
    #             res[i] = max_prod // nums[i]
            
    #     return res