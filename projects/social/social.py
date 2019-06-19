

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0  # Used as a counter for total number of users in social graph
        self.users = {}  # Individiual nodes in the graph
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Creates a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)  # intantiates a new user
        self.friendships[self.lastID] = set()  # creates an empty node in the graph (with no connections)

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # (1) Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # (2) Create a graph
        sg = SocialGraph()
        # (3) Add users
        # (3a) Use for loop to iterate through 'numUsers'
        for user in range(numUsers):
            self.addUser(user)
        # (3b) For each user, randomly generate a number of friendships based on the
        #      'avgFriendships' parameter
        # (4) Check to see that graph has been created and populated properly
        
        # sg.populateGraph(10, 2)
        # print(sg.friendships)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
