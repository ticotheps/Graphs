#----------------------Understanding the Problem-------------------------
#  ancestor = any node that comes before a specific node
#  earliest-known ancestor = the furthest ancestor node

#  Problem: 
    #  -Expected input: ID of input node
    #  -Expected output: ID of earliest-known ancestor
        #  -If there is a tie between two earliest-known ancestors,
        #   return the lower numeric ID.
        #  -If there is no ancestors, return -1.

#---------------------------Devising a Plan------------------------------

#  (1) Create an empty set to store visited nodes
#  (2) Create an empty Queue and enqueue the input node
#  (3) While the queue is NOT empty...
    #  (a) Dequeue the first node and set equal to a variable, "v"
    #  (b) If "v" is not in the list of visited nodes...
    #  (c) Then, add it to the set of visited nodes
    #  (d) Print the node
    #  (e) Use a for loop to find the node's neighbors and add them to the
    #      back of the queue
#  If there are no ancestors, return -1

#------------------------Implementing the Plan---------------------------

from util import Queue

class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        self.vertices[vertex] = set()  # Creates a node in the set
        
    def add_edge(self, v1, v2):
        """
        Adds a directed edge to the graph.
        """
        #  If both vertices exist in the graph (the set)...
        if v1 in self.vertices and v2 in self.vertices:  
            #  Add an edge from v1 to v2
            self.vertices[v2].add(v1)
        #  If both vertices DO NOT exist in the graph (the set)...
        else:
            #  Thow an error
            raise IndexError("That vertex does not exist!")
     
    def earliest_ancestor(self, starting_vertex):
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                visited.add(current)
                # print(current)
                for neighbor in self.vertices[current]:
                    q.enqueue(neighbor)
        if current == starting_vertex:
            print(f"starting_vertex: {starting_vertex}; earliest known ancestor: ", -1)
        else:
            print(f"starting_vertex: {starting_vertex}; earliest known ancestor: ", current)
        
if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(10)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(4)
    graph.add_vertex(11)
    graph.add_vertex(3)
    graph.add_vertex(5)
    graph.add_vertex(8)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(9)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(4, 5)
    graph.add_edge(4, 8)
    graph.add_edge(8, 9)
    graph.add_edge(11, 8)
    graph.add_edge(10, 1)

    graph.earliest_ancestor(10)  #  Should print -1
    graph.earliest_ancestor(1)  #  Should print 10
    graph.earliest_ancestor(3)  #  Should print 10
    graph.earliest_ancestor(6)  #  Should print 10
    graph.earliest_ancestor(2)  #  Should print -1
    graph.earliest_ancestor(5)  #  Should print 4
    graph.earliest_ancestor(4)  #  Should print -1
    graph.earliest_ancestor(7)  #  Should print 4
    graph.earliest_ancestor(8)  #  Should print 4
    graph.earliest_ancestor(9)  #  Should print 4
    graph.earliest_ancestor(11)  #  Should print -1

#-------------------------Reflecting/Iterating---------------------------