"""
   This code implements a Depth First Search of a Graph using a class
"""
from collections import defaultdict

class Graph:

 def __init__(self):

    self.graph = defaultdict(list)
    self.nodes = 4

 def addEdge(self,u,v):
    
    self.graph[u].append(v)


 def dfs(self, visited, node):

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in self.graph[node]:
            self.dfs(visited, neighbor)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is Breadth First Traversal:(starting from vertex 2)")
visited = set()
g.dfs(visited, 2)