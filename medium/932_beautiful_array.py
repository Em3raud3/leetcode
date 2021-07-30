class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        permutation = list()
        i = 0

        while len(permutation) != n:
            if i == 0:
                permutation = [1]

            else:
                for num in range(len(permutation)):

                    if num == 0:
                        odd = list()
                        even = list()

                    odd_num = (2*permutation[num]) - 1
                    even_num = (2*permutation[num])

                    if odd_num <= n:
                        odd.append(odd_num)

                    if even_num <= n:
                        even.append(even_num)

                    if num == len(permutation) - 1:
                        permutation = odd + even  # ! need a better way to do this part

            i += 1

        return(permutation)
