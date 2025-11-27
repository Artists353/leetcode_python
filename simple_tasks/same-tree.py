# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q is None and p is None:
            return True 
        if q is None or p is None:
            return False 
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Values are not equal, they are not identical
        return False
        


p = [1,2,3]
q = [1,2,3]
solution = Solution()
print(solution.isSameTree(p, q))
        
