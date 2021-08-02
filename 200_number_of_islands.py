class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        island = 0
        visited = []

        for i in range(m):
            visited.append([False for _ in range(n)])

        def check_adjacent(row, col, table, visitation):
            #! Check Right
            try:
                if table[row][col + 1] and table[row][col + 1] == "1":
                    table[row][col + 1] = "0"
                    check_adjacent(row, col + 1, table, visitation)
            except Exception:
                pass

            #! Check Down
            try:
                if table[row + 1][col] and table[row + 1][col] == "1":
                    table[row + 1][col] = "0"
                    check_adjacent(row + 1, col, table, visitation)
            except Exception:
                pass

            #! Check Left
            try:
                if visitation[row][col - 1] == False and col != 0:
                    if table[row][col - 1] == "1":
                        table[row][col - 1] = "0"
                        check_adjacent(row, col - 1, table, visitation)

            except Exception:
                pass

                #! Check Up
            try:
                if visitation[row - 1][col] == False and row != 0:
                    if table[row - 1][col] == "1":
                        table[row - 1][col] = "0"
                        check_adjacent(row - 1, col, table, visitation)
            except Exception:
                pass

        if not grid:
            print(0)
            exit()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    visited[i][j] = True
                    check_adjacent(i, j, grid, visited)

        return(island)
