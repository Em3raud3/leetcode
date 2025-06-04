# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res = ""
        keyset = {}

        # initalize with min with infinity
        shortest = float("inf")

        # count of unique characters in t
        for i in t:
            keyset[i] = keyset.get(i, 0) + 1

        currentkeys = {}
        need = len(keyset)
        have = 0

        left = 0

        for i in range(len(s)):
            if s[i] in keyset:
                currentkeys[s[i]] == currentkeys.get(s[i], 0) + 1

                if currentkeys.get(s[i]) == keyset.get(s[i]):
                    have += 1

            if have == need:
                while s[left] not in keyset:
                    left += 1

                if len(s[left, i]) < shortest:
                    shortest = len(s[left, i])
                    res = s[left, i]

                currentkeys[s[left]] == currentkeys.get(s[left]) - 1

                if currentkeys.get([s[left]]) < keyset.get(s[left]):
                    have -= 1

                left = +1

        return res


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    result = solution.minWindow(s, t)
    print(result)  # Expected output: "BANC"
