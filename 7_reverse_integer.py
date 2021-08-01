class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        x_str = list(x_str)

        if x < -2**31 or x > (2**31) - 1:
            return 0

        else:
            if x < 0:
                x_str.pop(0)
                x_str.reverse()
                x = "-"

                while True:
                    if x_str[0] == "0":
                        x_str.pop(0)

                    else:
                        break

                for i in x_str:
                    x += i

                x = int(x)

                if x < -2**31 or x > (2**31) - 1:
                    return 0

                else:
                    return x

            elif x == 0:
                return 0

            else:
                x_str.reverse()
                x = ""

                while True:
                    if x_str[0] == "0":
                        x_str.pop(0)

                    else:
                        break

                for i in x_str:
                    x += i

                x = int(x)

                if x < -2**31 or x > (2**31) - 1:
                    return 0

                else:
                    return x
