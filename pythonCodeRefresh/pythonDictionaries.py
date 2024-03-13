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
<<<<<<< HEAD
print("Desctructering segment")
t = 1, 2
x, y = t
print(x, y)
=======
print("Destructuring segment")
t = 1, 2
x, y = t
print(x, y)

# remember this dictionary
# studentAttendance = {"Bob": 100, "Fred": 95, "John": 80, "Zach": 75}
# turn studentAttendance into a list
print(list(studentAttendance.items()))

for student, attendance in studentAttendance.items():
    print(f"{student} : {attendance}")

for t in studentAttendance.items():
    # print(f"Destructuring list {student}: {attendance}")
    print(t)

peopleAndProfessions = [("Tom", 47, "Contractor"), ("Jim", 30, "Chef"), ("Chris", 25, "Salesman"),
                        ("A", 15, "Model")]
# if I don't care about age then I can use _ instead of identifying the age
for name, _, profession in peopleAndProfessions:
    print(f"Name: {name}, Profession: {profession}")

# take apart elements in a list
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(*tail)
>>>>>>> eb3025c (format fixes)
