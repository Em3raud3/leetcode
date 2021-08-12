class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = list()

        def dfs(left, right, string: str):
            if left == 0 and right == 0:
                res.append((string))
                return

            if right == left and right > 0:
                dfs(left - 1, right, string + "(")

            if len(string) != 0:
                if string[-1] == ")" and left > 0:
                    dfs(left - 1, right, string + "(")

            if left < right and left > 0:
                dfs(left - 1, right, string + "(")

            if left < right:
                dfs(left, right - 1, string + ")")

        dfs(n, n, "")

        return [y for y in {x for x in res}]
