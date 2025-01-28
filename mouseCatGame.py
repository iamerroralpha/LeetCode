#%%
from typing import List
from functools import lru_cache

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2

        @lru_cache(None)
        def dfs(mouse, cat, turn):
            # Base cases
            if mouse == 0:  # Mouse wins by reaching the Hole
                return MOUSE_WIN
            if cat == mouse:  # Cat wins by catching the Mouse
                return CAT_WIN
            if turn >= 2 * len(graph):  # Limit for repeated states
                return DRAW

            if turn % 2 == 0:  # Mouse's turn
                result = CAT_WIN  # Assume Cat wins unless Mouse finds a better move
                for next_move in graph[mouse]:
                    outcome = dfs(next_move, cat, turn + 1)
                    if outcome == MOUSE_WIN:
                        return MOUSE_WIN  # Mouse has a winning strategy
                    if outcome == DRAW:
                        result = DRAW  # Mouse forces a draw if no win
                return result
            else:  # Cat's turn
                result = MOUSE_WIN  # Assume Mouse wins unless Cat finds a better move
                for next_move in graph[cat]:
                    if next_move == 0:  # Cat can't go to the Hole
                        continue
                    outcome = dfs(mouse, next_move, turn + 1)
                    if outcome == CAT_WIN:
                        return CAT_WIN  # Cat has a winning strategy
                    if outcome == DRAW:
                        result = DRAW  # Cat forces a draw if no win
                return result

        return dfs(1, 2, 0)
    
#%%
graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
soltn = Solution()
print(soltn.catMouseGame(graph))
# %%
graph = [[1,3],[0],[3],[0,2]]
print(soltn.catMouseGame(graph))
# %%
