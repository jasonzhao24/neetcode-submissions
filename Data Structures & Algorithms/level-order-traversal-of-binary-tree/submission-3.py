# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        elif root.right is None and root.left is None:
            return [[root.val]]
        q = deque([root])
        result = []
        result.append([root.val])
        while q:
            row = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    row.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    row.append(node.right.val)
                    q.append(node.right)
            if row:
                result.append(row)
        return result

                
            
