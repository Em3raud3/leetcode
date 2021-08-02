class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) == 1 or numRows == 1:
            return s

        s = list(s)
        full_index = [_ for _ in range(numRows)]
        last_half = [_ for _ in range(numRows - 1)]
        last_half.reverse()
        last_half.pop()
        full_index = full_index + last_half

        lengths = len(s)
        lengthi = len(full_index)
        copies = lengths//lengthi
        if lengths % lengthi != 0:
            copies += 1

        full_index = full_index * copies
        arrays = [[] for _ in range(numRows)]

        for letter, index in zip(s, full_index):
            arrays[index].append(letter)

        answer = ""

        for i in arrays:
            for j in i:
                answer += j

        return answer
