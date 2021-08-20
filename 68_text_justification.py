class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        curr_length = 0
        word_count = 0

        ans = []
        arr = []

        def space_function(ans, arr, maxWidth, word_count):

            space = " "
            spaces = maxWidth - word_count
            num_words = len(arr) - 1 if len(arr) > 1 else 1
            left_extra = spaces % num_words
            normal_spacing = spaces // num_words
            to_add = ""

            for index, i in enumerate(arr):
                if left_extra > 0:
                    to_add += i + (normal_spacing + 1)*space
                    left_extra -= 1

                elif index < len(arr) - 1 and left_extra == 0:
                    to_add += i + normal_spacing*space

                else:
                    to_add += i

            if len(to_add) < maxWidth:
                to_add = to_add + (maxWidth - len(to_add))*" "

            ans.append(to_add)
            return

        while True:

            if words:
                if curr_length + len(words[0]) <= maxWidth and words:
                    word = words.pop(0)
                    curr_length += len(word) + 1
                    word_count += len(word)
                    arr.append(word)

                else:
                    space_function(ans, arr, maxWidth, word_count)
                    curr_length = 0
                    word_count = 0
                    arr.clear()

            else:
                string = ""
                for i in arr:
                    string += i + " "

                if len(string) > maxWidth:
                    string = string.rstrip()

                else:
                    string = string + (maxWidth - len(string))*" "
                ans.append(string)
                break



        return ans