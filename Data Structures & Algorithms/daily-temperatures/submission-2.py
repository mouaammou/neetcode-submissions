class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = []
    #     n = len(temperatures)
    #     for i in range(n):
    #         length = 0
    #         j = i + 1
    #         while j < n:
    #             if temperatures[i] < temperatures[j]:
    #                 length += 1
    #                 break
    #             if j == n - 1:
    #                 length = 0
    #             else:
    #                 length += 1
    #             j += 1
    #         res.append(length)
    #     return res


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, _ = stack.pop()
                res[index] = i - index
            stack.append([i, temp])
        return res