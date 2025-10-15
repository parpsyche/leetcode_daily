# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        values = [None]*101
        level = 0
        stack = [(root,level)]
        while(stack):
            node, rank = stack.pop()
            level = max(level,rank)
            if not node:
                continue
            values[rank] = node.val
            if node.right:
                stack.append((node.right, rank+1))                
            if node.left:
                stack.append((node.left, rank+1))                

        return values[:level+1]
