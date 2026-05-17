class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_nums = numbers[left] + numbers[right]
            if sum_nums == target:
                return [left + 1,right + 1]

            if sum_nums > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]