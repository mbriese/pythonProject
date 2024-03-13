# CRUD operations in python Dictionaries
# Dictionaries are a key value pair
friend_age = {"Rolf": 24}
moreFriends_andAges = {"Adam": 15, "Mary": 50, "Frank ": 30}
# access elements in the dictionary using subscripts
print(moreFriends_andAges["Adam"])

# adding to a dictionary
moreFriends_andAges["Bob"] = 35

# update a dictionary element
moreFriends_andAges["Mary"] = 35

print(moreFriends_andAges)

# delete an element from a dictionary
del moreFriends_andAges["Bob"]

print(moreFriends_andAges)

# make a dictionary of friends
friends = [
    {"name": "Tyson", "age": 65},
    {"name": "James", "age": 50},
    {"name": "William", "age": 45}
]
print(friends)
print(friends[1])
print(friends[1]["name"])

# more dictionary playground
studentAttendance = {"Bob": 100, "Fred": 95, "John": 80, "Zach": 75}
# access individual items in Dictionary
for student, attendance in studentAttendance.items():
    print(f"Student {student} attended class {attendance} times")
if "Bob" in studentAttendance:
    print(f"Bob: attended class {studentAttendance['Bob']}")
else:
    print("Bob is not a student in this class")
# get the average attendance for the class
classAttendanceValues = sum(studentAttendance.values()) / len(studentAttendance)
print(f" The avg attendance is {classAttendanceValues}")

# Destructuring Variables and tuples
# Tuples can be assigned to variables
print("Desctructering segment")
t = 1, 2
x, y = t
print(x, y)
