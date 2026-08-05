class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_ = len(temperatures)
        res = [0] * len_

        stack = [(0, temperatures[0])]

        for i in range(1, len_):
            
            while stack and temperatures[i] > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temperatures[i]))
        

        return res