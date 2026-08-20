# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        if not root:
            return 0
        q = deque([(root,root.val)]) ## In the queue is the node and its value, so we can track the value
        while q:
            node, curr_max = q.popleft() 
            if node.val >= curr_max: ## Check if the value of our node is greater than the max val
                good+=1
            new_max = max(curr_max,node.val) ## Find new max
            if node.left:
                q.append((node.left,new_max))
            if node.right:
                q.append((node.right,new_max))
        return good
