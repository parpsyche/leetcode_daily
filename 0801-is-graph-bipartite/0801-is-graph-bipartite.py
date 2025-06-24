from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)  # Number of nodes in the graph
        colors = [-1] * n  # Initialize all nodes as uncolored (-1)
        isPossible = True  # Variable to track if bipartite coloring is possible

        def dfs(node, color):
            nonlocal isPossible
            if not isPossible:
                return
            
            colors[node] = color  # Assign color to the current node
            for neighbor in graph[node]:  # Explore all neighbors
                if colors[neighbor] == -1:  # If the neighbor is uncolored
                    dfs(neighbor, color ^ 1)  # Assign the opposite color
                elif colors[neighbor] == colors[node]:  # If same color is found
                    isPossible = False  # Graph is not bipartite

        # Check for all nodes (handling disconnected graphs)
        for i in range(n):
            if not isPossible:
                return False
            if colors[i] == -1:  # Not visited yet
                dfs(i, 0)  # Start DFS from this node with color 0

        return True  # If we reach here, the graph is bipartite