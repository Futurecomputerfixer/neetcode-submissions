# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, Max):
            ans = 0
            if node.val >= Max:  
                ans = 1
                Max = node.val
            
            l = dfs(node.left, Max) if node.left else 0
            r = dfs(node.right, Max) if node.right else 0

            return ans + l + r
        
        return dfs(root, -101)
