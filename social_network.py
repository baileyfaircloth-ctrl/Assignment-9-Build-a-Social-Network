class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} is already in the network.")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"{person1_name} does not exist.")
            return

        if person2_name not in self.people:
            print(f"{person2_name} does not exist.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name}: {', '.join(friend_names)}")


# Test your code here
network = SocialNetwork()

# Add 6 people
network.add_person("Alice")
network.add_person("Bob")
network.add_person("Charlie")
network.add_person("David")
network.add_person("Emma")
network.add_person("Frank")

# Add 8 friendships
network.add_friendship("Alice", "Bob")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Bob", "David")
network.add_friendship("Charlie", "Emma")
network.add_friendship("David", "Frank")
network.add_friendship("Emma", "Frank")
network.add_friendship("Alice", "Emma")
network.add_friendship("Bob", "Frank")

# Test duplicate person
network.add_person("Alice")

# Test nonexistent person
network.add_friendship("Alice", "George")

# Print the network
network.print_network()
