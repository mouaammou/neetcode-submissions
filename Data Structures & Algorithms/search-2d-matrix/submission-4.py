class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        n = rows * cols

        left = 0
        right = n - 1
        
        while left <= right:
            index = (left + right) // 2
            row = index // cols
            col = index % cols

            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                left = index + 1
            else:
                right = index - 1

        return False

            