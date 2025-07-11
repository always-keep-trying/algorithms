from collections import defaultdict


def recursive_method(tree, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        visited.add(node)
    print(node)
    for x in tree[node]:
        if x not in visited:
            recursive_method(tree, x, visited)


def iterative_method(tree, start):
    visited = set() # to track visited nodes
    stack = [start] # places to visit

    while stack:
        node = stack.pop() # get the last element that was added
        if node not in visited:
            visited.add(node) # track where you have visited
            print(node)
            stack.extend(reversed(tree[node])) # add child nodes to stack


class Graph:
    # DFS for a Graph (not a tree)
    def __init__(self):
        # initialize the graph with a default dict, the values will be lists
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        print(f"Added Edge ({u},{v})")

    def buildEdges(self, adj):
        # build graph
        for i, v in enumerate(adj):
            for x in v:
                self.addEdge(i, x)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        # recursive method
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()

        self.DFSUtil(v, visited)


def tree_main():
    # tree has parent and child relationship: hierarchical data
    # Define the decision tree as a dictionary
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': [], 'I': [], 'J': [], 'K': [],
        'L': [], 'M': [], 'N': [], 'O': []
    }
    # recursive_method(tree, 'A')
    iterative_method(tree, 'A')

def graph_main():
    # https://www.geeksforgeeks.org/python/python-program-for-depth-first-search-or-dfs-for-a-graph/
    # graph
    adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    print("Example 1")
    g = Graph()
    g.buildEdges(adj)
    g.DFS(1)

    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print("Example 2")
    g2 = Graph()
    g2.buildEdges(adj)
    g2.DFS(0)

if __name__ == "__main__":
    print("Tree: ")
    tree_main()

    print("Graph: ")
    graph_main()
