class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            visited = set()
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                if board[i][j] in visited:
                    return False
                visited.add(board[i][j])

        for i in range(cols):
            visited = set()
            for j in range(rows):
                if board[j][i] == '.':
                    continue
                if board[j][i] in visited:
                    return False
                visited.add(board[j][i])

        L = [[set() for i in range(3)] for i in range(3)]
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    continue
                if (board[x][y] in L[x//3][y//3]):
                        return (False)
                L[x//3][y//3].add(board[x][y])
        return True
                
