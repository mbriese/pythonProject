# refresh knowledge of higher order code
# sets do not guarantee the order is maintained
listOfFriends = ["Anna", "Jack", "Mary"]  # you may add modify remove items from list

# tuples do not require parens
tupleOfFriends = ("Anna", "Jack", "Mary")  # you may not add or remove items from tuples
tupleOf1Friend = "James",
tupleOf2Friends = "Jack", "Jill"
tupleOf2Numbers = 1, 3


setOfFriends = {"Anna", "Jack", "Mary"}  # no duplicates in sets, may add and remove from sets

# subscript notation to access element in lists sets and tuples
print(f"original list of Friends {listOfFriends}")
print(listOfFriends[0])  # will print "Anna"
listOfFriends[0] = "Mindi"
print(f"modified list of Friends {listOfFriends}")
listOfFriends.append("Steven")
print(f"I found a new Friend {listOfFriends}")

listOfFriends.remove("Steven")
print(f"I lost a Friends {listOfFriends}")

print(f"Here is my set of friends {setOfFriends}")
setOfFriends.add("Quia")
print(f"I added to my set of friends {setOfFriends}")

# listOfTuples requires parens
listOfTuplesWithNumbers = [(1, 5), (2, 6)]
# remember without parens its just a list
listOfNumbers = [1 , 5, 2, 6]