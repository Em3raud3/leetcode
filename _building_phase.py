from collections import deque

mat = [[0, 0, 0],
       [0, 1, 0],
       [1, 1, 1]]

queue = deque()

for i, row in enumerate(mat):
    print(i)

print()
