class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recurse(l, r):
            if l > r: return -1
            elif l == r: return False if matrix[l//len(matrix[0])][l % len(matrix[0])] != target else True
            else:
                m = (l+r) // 2
                return recurse(l, m) or recurse(m+1, r)
        
        return recurse(0, len(matrix)*len(matrix[0])-1)