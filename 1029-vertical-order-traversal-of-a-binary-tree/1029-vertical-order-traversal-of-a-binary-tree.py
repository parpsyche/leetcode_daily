from collections import deque, defaultdict
from typing import List, Optional

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Track (depth, value) for each horizontal distance (hd)
        map = defaultdict(list)
        queue = deque([(root, 0, 0)])  # (node, hd, depth)
        
        while queue:
            node, hd, depth = queue.popleft()
            map[hd].append((depth, node.val))
            if node.left:
                queue.append((node.left, hd - 1, depth + 1))
            if node.right:
                queue.append((node.right, hd + 1, depth + 1))
        
        # Sort by hd, then by depth, then by value
        return [
            [val for _, val in sorted(map[hd], key=lambda x: (x[0], x[1]))] 
            for hd in sorted(map.keys())
        ]