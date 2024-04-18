from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # best clean solution
        """
        Square indices = r//3 and c//3 because e.g. [0,2] gives 0//3 = 0, 2 // 3 = 0 
        so we know that analyzed square is top left one, 
        [4,8] 4//3 = 1, 8//3 = 2 so we know analyzed square is right square in the middle 
                          |__0__|__1__|__2__|  <- square indices
                       _  |0|1|2|3|4|5|6|7|8|  <- columns indices
                      | |0|_|_|_|_|_|_|_|_|_|
                      |0|1|_|_|_|_|_|_|_|_|_|
                      |_|2|_|_|_|_|_|_|_|_|_|
                      | |3|_|_|_|_|_|_|_|_|_|
                      |1|4|_|_|_|_|_|_|_|_|_|
                      |_|5|_|_|_|_|_|_|_|_|_|
                      | |6|_|_|_|_|_|_|_|_|_|
                      |2|7|_|_|_|_|_|_|_|_|_|
                      |_|8|_|_|_|_|_|_|_|_|_|
        square indices-^ ^-row indices
                         
        """
        cols = defaultdict(set) # could be also List[Set]
        rows = defaultdict(set) # could be also List[Set]
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]): 
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


        #my solution
        EMPTY = "."
        CLEAN = {i: 0 for i in range(1, 10)}
        fields = CLEAN.copy()
        for row in board:
            for value in row:
                if value != EMPTY:
                    value = int(value)
                    if fields[value] == 1:
                        return False
                    else:
                        fields[value] = 1
            fields = CLEAN.copy()
        
        for val_index in range(0, 9):
            for col_index in range(0, 9):
                value = board[col_index][val_index]
                if value != EMPTY:
                    value = int(value)
                    if fields[value] == 1:
                        return False
                    else:
                        fields[value] = 1
            fields = CLEAN.copy()

        for cube_index in range(0, 9, 3):
            col_index = 0
            left = 3
            while left > 0:
                for r_index in range(cube_index, cube_index + 3):
                    for c_index in range(col_index, col_index + 3):
                        value = board[r_index][c_index]
                        if value != EMPTY:
                            value = int(value)
                            if fields[value] == 1:
                                return False
                            else:
                                fields[value] = 1
                col_index += 3
                left -= 1
                fields = CLEAN.copy()

        return True