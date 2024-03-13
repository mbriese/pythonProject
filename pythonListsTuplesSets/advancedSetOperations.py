# Fun with sets - comparison
setOfFriends = {"Anna", "Jack", "Mary"}  # no duplicates in sets, may add and remove from sets
outOfTownFriends = {"Mary", "Anna"}

localFriends = setOfFriends.difference(outOfTownFriends)
print(f"these friends are still in town {localFriends}")
emptyFriends = outOfTownFriends.difference(setOfFriends)
print(f"the difference between outOfTown friends& localFriends is an empty set {emptyFriends}")
newFriends = {"Dick", "Jane", "Spot"}
englishStudentFriends = {"Anna", "Mary", "Jane"}
mathStudentFriends = {"Jack", "Dick", "Jane"}
print(f"new friends is an this set set {newFriends}")
allMyFriends = setOfFriends.union(newFriends)
print(f"all my friends is this set set {allMyFriends}")
friendsIntersection = englishStudentFriends.intersection(mathStudentFriends)
print(f"my friends in math and english are {friendsIntersection}")

# little test from course
# my tuple surprise need to add "," to show it is not a mathematical operator
my_list = [50, 37, 13]
print(f"my list {my_list}")
# Create a tuple, called my_tuple, with a single value in it
my_tuple = (1,)
print(f"my list {my_tuple}")
# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 9, 12, 77}
intersectS1andS2 = set1.intersection(set2)
print(f"s1 intersect s2 {intersectS1andS2}")
