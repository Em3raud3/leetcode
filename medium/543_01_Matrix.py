from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        # approach: use BFS start from all 0s to update all non-zero elements

        m = len(matrix)
        n = len(matrix[0])

        queue = deque()
