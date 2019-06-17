#-----------------------------DAY 1: GRAPHS------------------------------

#  TIP: MEMORIZE the algorithms for:
    #  -BREADTH FIRST SEARCH
    #  -DEPTH FIRST SEARCH
     
#  WHY? 
    #  -To MORE easily recognize this data structure when encountering it
    #  -To conserve brain power when solving problems using these 
    #   algorigthms.

#  What is a 'GRAPH'?
    #  -Graphs are data structures that are used to represent
    #   relationships.
    #  -Runtime complexity of Adjacency List: O(n * e), 
        #  -In this case, n = nodes, e = average # of edges per vertex,
        #   E = total number of edges
    #  -Runtime complexity of Adjacency Matrix: O(n^2)
    
#  What are graphs composed of?
    #  -Nodes (AKA "Vertices" or "Vertexes")
        #  -Holds values
        #  -i.e. - friends on Facebook
    #  -Edges (can be arrows or lines)
        #  -Used to describe kinds of relationships between two nodes
    #  -Graphs can be either: 
        #  -WEIGHTED or UNWEIGHTED:
            #  -WEIGHTED graph = a graph with specficied values on each   
            #   edge that emphasize the importance/priority of that edge
            #   in comparison to other edges. 
                #  -i.e. - Google maps uses weighted graphs to help users
                #   find the shortest path between two points on a map.
            #  -UNWEIGHTED graph = a graph WITHOUT specficed values on   
            #   each edge to emphasize the importance/priority of that edge
            #   in comparison to other edges. 
        #  -DIRECTED or UNDIRECTED:
            #  -DIRECTED graph = demonstrates a relationship between  
            #   two nodes where only ONE node is directly affected by
            #   their relationship with the other. 
                #  -i.e. - Your Twitter account and your followers
                    #  -Just because someone follows you on Twitter does
                    #   NOT mean that you must follow them
            #  -UNDIRECTED graph = demonstrates a bi-directional 
            #   relationship between two nodes where only BOTH nodes are 
            #   directly affected by their relationship with one other.
                #  -i.e. - Friends on Facebook
                    #  -When someone is your friend on Facebook, you are
                    #   automatically assumed to be THEIR friend as well.    
        #  -CYCLIC or ACYCLIC:
            #  -CYCLIC graph = a graph that contains related nodes where
            #   you can travel along the edges and end up at a previously-
            #   visited node.
            #  -ACYCLIC graph = a graph that DOES not contain any related
            #   nodes where you can travel along the edges and end up at 
            #   a previously-visited node.
        #  -SPARSE or DENSE:
            #  -SPARSE graph = a graph that has a low number of edges 
            #   for each node.
            #  -DENSE graph = a graph that has a high number of edges 
            #   for each node.   

#  PROBLEM SOLVING WITH GRAPHS:
    #  (1)  Understand/Translate the Problem
    #  (2)  Create the graph
    #  (3)  Traverse the graph          