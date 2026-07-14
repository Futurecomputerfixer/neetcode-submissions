# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node, res):
            if not node:
                return (0, 0)
            
            (h1, res1) = recurse(node.left, res)
            (h2, res2) = recurse(node.right, res)

            dia = h1+h2
            h = max(h1, h2) + 1

            return (h, max(dia, max(max(res1, res2), res)))
        
        (_, ans) = recurse(root, 0)
        return ans