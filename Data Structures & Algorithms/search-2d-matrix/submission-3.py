class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) * len(matrix[0])
        left = 0
        right = n - 1
        

        while left <= right:
            mid = (left + right) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                right = mid - 1

        return False
        