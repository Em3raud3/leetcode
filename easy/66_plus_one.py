class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits.reverse()

        for i in range(len(digits)):
            if i == 0:
                digits[i] += 1

            if digits[i] >= 10:
                digits[i] -= 10

                try:
                    digits[i+1] = digits[i+1] + 1

                except Exception:
                    digits.append(1)

        digits.reverse()

        print(digits)

        return digits
