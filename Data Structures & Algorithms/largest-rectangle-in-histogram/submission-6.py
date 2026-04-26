class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     max_area = 0
    #     n = len(heights)
    #     for i in range(n - 1, -1, -1):
    #         sub_array = heights[i:]

    #         for j in range(len(sub_array)):
    #             # print(sub_array[:j+1])
    #             new_sub = sub_array[: j + 1]
    #             max_area = max(max_area, len(new_sub) * min(new_sub))

    #     return max_area
   def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)        
        
        for i in range(n):
            curr_min = heights[i]
            for j in range(i, n):
                curr_min = min(curr_min, heights[j])
                max_area = max(max_area, curr_min * (j - i + 1))
        return max_area