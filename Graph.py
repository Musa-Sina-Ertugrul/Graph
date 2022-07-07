from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []


class Graph:
    def __init__(self):
        self.visited = []
        self.nodes = []
        self.level = {}
        self.parent = {}
        self.queue = Queue()
        self.bfs_traversal_output = []
        self.path = []

    def add_node(self, node):
        self.nodes.append(node)

    def remove(self, data):
        self.nodes.remove(data)
        for node in self.nodes:
            node.edges.remove(data)

    @staticmethod
    def add_edge(node1, node2):
        node1.edges.append(node2)
        node2.edges.append(node1)

    def dfs(self, data):
        if data not in self.nodes:
            self.visited.append(data)
            print(data.data)
            for node in self.nodes:
                for edge in node.edges:
                    self.dfs(edge)

    def bfs_init(self):
        for node in self.nodes:
            self.visited[node.data] = False
            self.parent[node.data] = None
            self.level[node.data] = -1
        self.visited.clear()
        self.path.clear()

    def bfs(self, node):
        self.visited[node.data] = True
        self.level[node.data] = 0
        self.queue.put(node)
        while not self.queue.empty():
            u = self.queue.get()
            self.bfs_traversal_output.append(u)
            for v in u.edges:
                if not self.visited[v.data]:
                    self.visited[v.data] = True
                    self.parent[v.data] = u.data
                    self.level[v.data] = self.level[u.data] + 1
                    self.queue.put(v)
        print(self.bfs_traversal_output)

    def shortest(self, node):
        name = node.data
        while name is not None:
            self.path.append(name)
            name = self.parent[name]
        self.path.reverse()
        print(self.path)
