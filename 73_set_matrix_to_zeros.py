class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_row = set()
        zero_col = set()


        for index1, i in enumerate(matrix):
            for index2, j in enumerate(i):
                if j == 0:
                    zero_row.add(index1)
                    zero_col.add(index2)


        for i in zero_row:
            matrix[i] = [0]*len(matrix[0])

        for i in zero_col:
            for j in matrix:
                j[i] = 0