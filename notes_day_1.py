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
    
#  What are graphs composed of?
    #  -Nodes (AKA "Vertices")
        #  -Holds values
        #  -i.e. - friends on Facebook
    #  -Edges (looks like arrows)
        #  -Used to describe kinds of relationships
    #  -Graphs can be either: 
        #  -WEIGHTED or UNWEIGHTED:
        #  -DIRECTED or UNDIRECTED:
            #  -DIRECTED graph = demonstrates a relationship between  
            #   two nodes where only ONE node is directly affected by
            #   their relationship with the other. 
                #  -
                #  -i.e. - Your Twitter account and your followers
                    #  -Just because someone follows you on Twitter does
                    #   NOT mean that you must follow them
            #  -UNDIRECTED graph = demonstrates a relationship between  
            #   two nodes where only BOTH nodes are directly affected by
            #   their relationship with one other.
                #  -i.e. - Friends on Facebook
                    #  -When someone is your friend on Facebook, you are
                    #   automatically assumed to be THEIR friend as well.    
        #  -CYCLIC or ACYCLIC:
        #  -SPARSE or DENSE: