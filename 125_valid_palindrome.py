class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for letter in s:
            if letter.isalnum():
                new_string += letter.lower()


        return new_string == new_string[::-1]

