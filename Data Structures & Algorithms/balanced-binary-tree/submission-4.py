# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(node):
            if not node: return 0
            l, r = recurse(node.left), recurse(node.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l, r)+1
         
        return recurse(root) != -1
