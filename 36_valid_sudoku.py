class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        res = []
   
        for r, rv in enumerate(board):
            for c, val in enumerate(rv):
                if val != ".":
                    res += [(val, "row" + str(r)), (val, "col" + str(c)), (r//3, c//3, val)]
                    
        return len(res) == len(set(res))
