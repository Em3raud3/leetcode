class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        answer = ""

        answer += M[num//1000]
        num = num % 1000

        answer += C[num//100]
        num = num % 100

        answer += X[num//10]
        num = num % 10

        answer += I[num]

        return answer

    intToRoman(58)
