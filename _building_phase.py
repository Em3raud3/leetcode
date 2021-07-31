str = "abba"


def expand_from_middle(s, left, right):

    if not s or left > right:
        return 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return(right - left - 1)


mStr = ""

for i in range(len(str)):
    l1 = expand_from_middle(str, i, i)
    l2 = expand_from_middle(str, i, i + 1)
    l = max(l1, l2)


print(maxL)
