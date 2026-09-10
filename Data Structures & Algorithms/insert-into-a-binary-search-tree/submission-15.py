# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return TreeNode(val)
            if val > node.val:
                helper(node.right)
                if not node.right:
                    node.right = TreeNode(val)
            if val < node.val:
                helper(node.left)
                if not node.left:
                    node.left = TreeNode(val)
        if not root:
            return helper(root)
        helper(root)
        return root
