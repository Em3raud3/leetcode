class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        number = {"2": ["a", "b", "c"],
                  "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"],
                  "6": ["m", "n", "o"],
                  "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"],
                  "9": ["w", "x", "y", "z"]}

        size = len(digits)
        num_arry = [""] if digits else []

        # for i in digits:
        #     if i == "1" or i == "0":
        #         continue
        for num in digits:
            num_arry = [p + q for p in num_arry for q in number[num]]

        return num_arry
