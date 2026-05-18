class Solution:
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     left_max = [0] * n
    #     left_max[0] = height[0]
    #     for i in range(1, n):
    #         left_max[i] = max(left_max[i - 1], height[i])

    #     right_max = [0] * n
    #     right_max[n - 1] = height[n - 1]
    #     for i in range(n - 2, -1, -1):
    #         right_max[i] = max(right_max[i + 1], height[i])
    #     res = 0
    #     for i in range(n):

    #         res += min(left_max[i], right_max[i]) - height[i]

    #     return res

    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]
        water_trap = 0
        while left < right:
            if left_max < right_max:
                left += 1

                left_max = max(left_max, height[left])
                water_trap += left_max - height[left]
            else:
                right -= 1

                right_max = max(right_max, height[right])
                water_trap += right_max - height[right]

        return water_trap






