#%%
Input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


#%%


from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set(range(1, 10)) for _ in range(9)]
        cols = [set(range(1, 10)) for _ in range(9)]
        boxes = [set(range(1, 10)) for _ in range(9)]


        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[(i // 3) * 3 + j // 3].remove(num)

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':

                        box_index = (i // 3) * 3 + (j // 3)

                        possible_numbers = rows[i] & cols[j] & boxes[box_index]

                        for num in possible_numbers:

                            board[i][j] = str(num)
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxes[box_index].remove(num)


                            if backtrack():
                                return True

                            board[i][j] = '.'
                            rows[i].add(num)
                            cols[j].add(num)
                            boxes[box_index].add(num)

                        return False


            return True

        backtrack()
        print(board)


# %%
soln = Solution()
soln.solveSudoku(Input)
# %%
