class Solution:
    def romanToInt(self, s: str) -> int:

        s = list(s)
        s.reverse()
        roman = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

        index = roman[s[0]]
        sum = 0

        for i in s:
            if roman[i] < index:
                sum -= roman[i]

            else:
                sum += roman[i]
                index = roman[i]

        return sum
