from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {node: set() for node in range(numCourses)}

        for i, j in prerequisites:
            graph[i].add(j)

        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbour in graph.get(node, []):
                indegree.setdefault(neighbour, 0)
                indegree[neighbour] += 1

        start = [i for i in indegree if indegree[i]==0]
        queue = deque(start)
        print(queue)     
        order = []   
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neigh in graph.get(curr, []):
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if len(order) != numCourses:
            return []
        return order[::-1] 
