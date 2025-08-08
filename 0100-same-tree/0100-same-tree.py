# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None:
            return root2==None
        if root2 == None:
            return False
        if root1.val != root2.val:
            return False
        left_same = self.isSameTree(root1.left, root2.left)
        right_same = self.isSameTree(root1.right, root2.right)

        return left_same and right_same