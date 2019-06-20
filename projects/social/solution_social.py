import random
import time

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # O(n)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        possibleFriendships = []
        # Time Complexity: O(n^2)
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        friendshipsToCreate = random.sample(possibleFriendships, (numUsers * avgFriendships) // 2)
        # numFriendshipsToCreate = (numUsers * avgFriendships) // 2
        # random.shuffle(possibleFriendships)
        # friendshipsToCreate = possibleFriendships[:numFriendshipsToCreate]
        for friendship in friendshipsToCreate:
            self.addFriendship(friendship[0], friendship[1])


    def populateGraphLinear(self, numUsers, avgFriendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # O(n)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        targetFriendships = numUsers * avgFriendships
        totalFriendships = 0
        collisions = 0
        while totalFriendships < targetFriendships:
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)
            if self.addFriendship(userID, friendID):
                totalFriendships += 2
            else:
                collisions += 1
        print(f"COLLISIONS: {collisions}")



    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        visited = {}
        q.enqueue( [userID] )
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited[v] = path
                for neighbor in self.friendships[v]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':

    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraph(500, 499)
    end_time = time.time()
    print (f"Quadratic Runtime: {end_time - start_time} seconds")

    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraphLinear(500, 499)
    end_time = time.time()
    print (f"Linear Runtime: {end_time - start_time} seconds")

    # print(sg.friendships)
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
    # print(f"USERS IN EXTENDED SOCIAL NETWORK: {len(connections)}")
    # totalSeparation = 0
    # for connection in connections:
    #     totalSeparation += len(connections[connection])
    # print(f"AVG LENGTH OF SOCIAL CONNECTION: {totalSeparation / len(connections)}")