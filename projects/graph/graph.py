"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represents a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        self.vertices[vertex] = set()  #  (1) Creates a node or vertex in the set
    def add_edge(self, v1, v2):
        """
        Adds a directed edge to the graph.
        """
        #  If both vertices exist in the graph (the set)...
        if v1 in self.vertices and v2 in self.vertices:  
            #  Add an edge from v1 to v2
            self.vertices[v1].add(v2)
        #  If both vertices DO NOT exist in the graph (the set)...
        else:
            #  Thow an error
            raise IndexError("That vertex does not exist!")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #  (1) Create an empty Queue
        visited = set()
        #  (2) Create an empty set to store visited nodes
        q = Queue()
        q.enqueue(starting_vertex)
        #  (3) While the queue is not empty...
        while q.size() > 0:
            #  (a) Dequeue the first vertex
            v = q.dequeue()
            #  (b) If that vertex has not been visited...
            if v not in visited:
                #  (i) Mark it as visited
                visited.add(v)
                print(v)
                #  (ii) Then, add all of its neighbors to the 
                #       back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
             
        # Step-by-Step Process for bft   
        # visited = {1, 2, 3, 4, 5, 7, 6}
        # queue = []
        # print: 1, 2, 3, 4, 5, 7, 6
            
        # v = 
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #  ***Use a STACK instead of Queue
        #  (1) Create an empty STACK and push the starting vertex
        visited = set()
        #  (2) Create an empty set to store visited nodes
        s = Stack()
        s.push(starting_vertex)
        #  (3) While the queue is not empty...
        while s.size() > 0:
            #  (a) Pop the first vertex
            v = s.pop()
            #  (b) If that vertex has not been visited...
            if v not in visited:
                #  (i) Mark it as visited
                visited.add(v)
                print(v)
                #  (ii) Then, add all of its neighbors to the 
                #       back of the queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        #  (1) Create an empty set to store visited nodes
        #  (2) Create an empty Queue and enqueue A PATH TO the starting vertex
        #  (3) While the queue is not empty...
            #  (a) Dequeue the first PATH
            #  (b) GRAB THE VERTEX FROM THE END OF THE PATH
            #  (c) If that vertex has not been visited...
                #  (i) Mark it as visited
                #  (ii) Then, add A PATH TO all of its neighbors to the 
                #       back of the queue
                #  (iii) Copy the path
                #  (iv) Append the neighbor to the back of the copy
                #  (v) Enqueue the copy
                    
                    
                    
                    
                    
    # q = [ [1,2,4], [1,2,3,5]]
    # visited = {1, 2}
    
    # path = [1, 2, 3]
    # v = 3
    # path_copy = [1, 2, 3, 5]
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)  #  <== checks to make sure error handling works properly
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("---------------------------------------------")
    print("Vertices of the Graph:\n") 
    print(graph.vertices)
    print("\n---------------------------------------------")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Depth First TRAVERSAL path for (1, 6):\n",)
    graph.dft(1)
    print("\n", "---------------------------------------------")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Breadth First TRAVERSAL path for (1, 6):\n",)
    graph.bft(1)
    print("\n", "---------------------------------------------")

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Depth First TRAVERSAL (recursive) path for (1, 6):\n")
    graph.dft_recursive(1)
    print("\n", "---------------------------------------------")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Breadth First SEARCH path for (1, 6):\n")
    graph.bfs(1, 6)
    print("\n", "---------------------------------------------")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Depth First SEARCH path for (1, 6):\n")
    graph.dfs(1, 6)
    print("\n", "---------------------------------------------")
