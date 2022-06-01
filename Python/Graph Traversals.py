""" 
     Author: Byron Dowling
     Course: CMPS 4143 Contemporary Programming Languages 
     Semester: Fall 2021
     Assignment: In-Class Assignment: Graph Traversals
     Date: 11/22/2021

"""

from collections import defaultdict

class Graph:

    def __init__ (self):

        self.graph = defaultdict(list)
        self.nodes = 12


    def addEdge (self, u, v):

        self.graph[u].append(v)


    def BFS(self, s):

        visited = [False] * (self.nodes+1)
        #print(len(visited))

        q = []
        q.append(s)
        visited[s] = True

        while len(q)!=0:

            s = q.pop(0)
            print(s, end=" ")

        for i in self.graph[s]:

            if visited[i] == False:
                q.append(i)
                visited[i] = True



    def dfs(self, visited, node):

        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(visited, neighbor)


    def printGraph(self):
        print(self.graph)


g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)

g.addEdge(2, 4)
g.addEdge(2, 5)

g.addEdge(3, 6)
g.addEdge(3, 7)

g.addEdge(4, 8)
g.addEdge(4, 9)

g.addEdge(5, 10)
g.addEdge(6, 11)
g.addEdge(6, 12)


g.addEdge(3, 20)
g.addEdge(20, 15)
g.addEdge(20, 7)
g.addEdge(2, 0)
g.addEdge(3, 3)
g.printGraph()

print ("Following is Breadth First Traversal:  (starting from vertex 1)")
g.BFS(1)
print ("\nFollowing is Depth First Traversal:  (starting from vertex 1)")
visited = set()
g.dfs(visited, 1)