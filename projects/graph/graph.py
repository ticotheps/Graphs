"""
Simple graph implementation
"""
from util import Stack, Queue  #  These may come in handy

class Graph:
    """Represents a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        self.vertices[vertex] = set()  #  (1)  Creates a node or vertex in the set
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
        #  (1)  Create an empty Queue
        visited = set()
        #  (2)  Create an empty set to store visited nodes
        q = Queue()
        q.enqueue(starting_vertex)
        #  (3)  While the queue is not empty...
        while q.size() > 0:
            #  (a)  Dequeue the first vertex
            v = q.dequeue()
            #  (b)  If that vertex has not been visited...
            if v not in visited:
                #  (i)  Mark it as visited
                visited.add(v)
                print(v)
                #  (ii)  Then, add all of its neighbors to the 
                #        back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
             
        #  Step-by-Step Process for bft   
        #  visited = {1, 2, 3, 4, 5, 7, 6}
        #  queue = []
        #  print: 1, 2, 3, 4, 5, 7, 6
            
        # v = 
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #  ***Use a STACK instead of Queue
        #  (1)  Create an empty STACK to store our scheduled nodes to explore
        #       and push the starting vertex
        visited = set()
        #  (2)  Create an empty set to store visited nodes
        s = Stack()
        s.push(starting_vertex)
        #  (3)  While the stack is not empty...
        while s.size() > 0:
            #  (a)  Pop the first vertex
            v = s.pop()
            #  (b)  If that vertex has not been visited...
            if v not in visited:
                #  (i)  Mark it as visited
                visited.add(v)
                print(v)
                #  (ii)  Then, add all of its neighbors to the 
                #        back of the queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
    def dft_recursive(self, starting_vertex, path=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        path += [starting_vertex]
        
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in path:
                self.dft_recursive(neighbor, path)
        print(path)   
        
    def bfs(self, starting_vertex, destination_vertex):
        # BFS
        # Create an empty set to store visited nodes
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        # While the queue is not empty...
            # Dequeue the first PATH
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # IF VERTEX = TARGET, RETURN PATH
            # If that vertex has not been visited...
                # Mark it as visited
                # Then add A PATH TO all of its neighbors to the back of the queue
                    # Copy the path
                    # Append neighbor to the back of the copy
                    # Enqueue copy
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #  Create an empty set to store visited nodes
        visited = set()
        #  Create an empty queue and enqueue a path to the starting_vertex
        q = Queue()
        q.enqueue( [starting_vertex] )
        #  While the queue is not empty...
        while q.size() > 0:
            #  Dequeue the first path
            path = q.dequeue()
            #  Grab the vertex from the end of the path
            v = path[-1]
            #  If vertex == target, return path
            if v == destination_vertex:
                return path
            #  If that vertex has not been visited...
            if v not in visited:
                #  Mark it as visited
                visited.add(v)
                #  Then add a path to all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    #  Copy the path 
                    path_copy = list(path)
                    #  Append the neighbor to the back of the copy
                    path_copy.append(neighbor)
                    #  Enqueue copy
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #  Create an empty set to store visited nodes
        visited = set()
        #  Create an empty Stack and push A PATH TO the starting_vertex
        s = Stack()
        s.push( [starting_vertex] )
        #  While the stack is not empty...
        while s.size() > 0:
            #  Pop the first path
            path = s.pop()
            #  Grab the vertex from the end of the path
            v = path[-1]
            #  If vertex == target, return path
            if v == destination_vertex:
                return path
            #  If that vertex has not been visited...
            if v not in visited:
                #  Mark it as visited
                visited.add(v)
                #  Then add a path to all of its neighbors to the back of the stack
                for neighbor in self.vertices[v]:
                    #  Copy the path 
                    path_copy = list(path)
                    #  Append the neighbor to the back of the copy
                    path_copy.append(neighbor)
                    #  Push copy
                    s.push(path_copy)

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
    print("-----------*** START OF OUR PATH PRINTING ***------------")
    print("Vertices of the Graph:\n") 
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n", "------------Depth First TRAVERSAL------------")
    print("Nodes visited (in this order):\n")
    graph.dft(1)

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
    print("\n", "--------------Breadth First TRAVERSAL------------")
    print("Nodes visited (in this order):\n")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n", "---------Depth First TRAVERSAL (Recursive)---------")
    print("Nodes visited (in this order):\n")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\n", "-------------Breadth First SEARCH----------")
    print("Nodes visited (in this order):\n")
    graph.bfs(1, 6)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\n", "------------Depth First SEARCH-----------")
    print("Nodes visited (in this order):\n")
    graph.dfs(1, 6)
