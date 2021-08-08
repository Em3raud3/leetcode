"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        levels = [[root] if root else []]
        while levels[-1]:
            levels.append([child for node in levels[-1]
                          for child in node.children])
        return [[node.val for node in level] for level in levels[:-1]]
