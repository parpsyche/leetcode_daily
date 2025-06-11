"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from copy import deepcopy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return deepcopy(node)