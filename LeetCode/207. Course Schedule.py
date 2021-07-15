from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        def is_cycle(i):
            if visited[i] == -1: return False
            if visited[i] == 1: return True

            visited[i] = -1
            for j in graph[i]:
                if not is_cycle(j):
                    return False
            visited[i] = 1
            return True

        visited = [0]*numCourses
        graph = defaultdict(list)
        for second, first in prerequisites:
            graph[second].append(first)
            
        for i in range(numCourses):
            if not is_cycle(i):
                return False
        return True
