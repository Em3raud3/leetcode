# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        paths = list()
        curr = list()

        def findpath(root, sum, current, path):
            if not root:
                return

            current.append(root.val)

            if root.val == sum and not root.left and not root.right:
                paths.append(current)

            findpath(root.left, sum - root.val, copy.deepcopy(current), path)
            findpath(root.right, sum - root.val, copy.deepcopy(current), path)

        findpath(root, targetSum, curr, paths)

        return paths
