class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        islandID = 1
        m = len(grid)
        n = len(grid[0])
        visited = []
        values = {}
        maxsize = 0

        for i in range(m):
            visited.append([False for _ in range(n)])

        def check_adjacent(row, col, table, visitation, size, id):
            #! Check Right
            try:
                if table[row][col + 1] and table[row][col + 1] == 1:
                    table[row][col + 1] = id
                    size += 1
                    size = check_adjacent(
                        row, col + 1, table, visitation, size, id)
            except Exception:
                pass

            #! Check Down
            try:
                if table[row + 1][col] and table[row + 1][col] == 1:
                    table[row + 1][col] = id
                    size += 1
                    size = check_adjacent(
                        row + 1, col, table, visitation, size, id)
            except Exception:
                pass

            #! Check Left
            try:
                if visitation[row][col - 1] == False and col != 0:
                    if table[row][col - 1] == 1:
                        table[row][col - 1] = id
                        size += 1
                        size = check_adjacent(
                            row, col - 1, table, visitation, size, id)

            except Exception:
                pass

            #! Check Up
            try:
                if visitation[row - 1][col] == False and row != 0:
                    if table[row - 1][col] == 1:
                        table[row - 1][col] = id
                        size += 1
                        size = check_adjacent(
                            row - 1, col, table, visitation, size, id)
            except Exception:
                pass

            return size

        def sum_surrounding(row, col, table, val):
            to_sum = set()
            sum = 0

            #! sum right
            try:
                if table[row][col + 1] != 0:
                    to_sum.add(table[row][col + 1])
            except Exception:
                pass

            #! sum down
            try:
                if table[row + 1][col] != 0:
                    to_sum.add(table[row + 1][col])
            except Exception:
                pass

            #! sum left
            if (col > 0) and (table[row][col - 1] != 0):
                to_sum.add(table[row][col - 1])

            #! sum up
            if (row > 0) and (table[row - 1][col] != 0):
                to_sum.add(table[row - 1][col])

            for i in to_sum:
                sum += val[i]

            return sum

        if not grid:
            return 0

        checkfor0 = set()
        for i in grid:
            for j in i:
                checkfor0.add(j)

        if not (0 in checkfor0):
            return n*m

        if not (1 in checkfor0):
            return 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islandID += 1
                    grid[i][j] = islandID
                    localsize = check_adjacent(
                        i, j, grid, visited, 1, islandID)
                    values[islandID] = localsize

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    this = sum_surrounding(i, j, grid, values)
                    maxsize = max(maxsize, this)

        return(maxsize + 1)
