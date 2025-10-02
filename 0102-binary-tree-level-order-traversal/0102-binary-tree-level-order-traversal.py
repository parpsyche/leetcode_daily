# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        out = []
        if root:
            q.append(root)
            out.append([root.val])
        while(q):
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    level.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    q.append(curr.right)
            if level:
                out.append(level)
        return out

