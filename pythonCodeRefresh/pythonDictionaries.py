#   Some dictionary declarations
friend_age = {"Rolf": 25, "Mariam": 1}
moreFriends_andAges = {"Adam": 15, "Mary": 50, "Frank": 30}
#   Read Access items in dictionary by name
print(f'This is Adams age {moreFriends_andAges["Adam"]}')
moreFriends_andAges["Bob"] = 35
moreFriends_andAges["Mary"] = 35
print(f'the dictionary moreFriends_andAges {moreFriends_andAges}')
del moreFriends_andAges["Bob"]
print(moreFriends_andAges)
friends = [{"name": "Tyson", "age": 65}, {"name": "James", "age": 50}, {"name": "William", "age": 45}]
print(friends)
print(friends[1])
print(friends[1]["name"])
studentAttendance = {"Bob": 100, "Fred": 95, "John": 80, "Zach": 75}
for student, attendance in studentAttendance.items():
	print(f"Student {student} attended class {attendance} times")
if "Bob" in studentAttendance:
	print(f"Bob: attended class {studentAttendance['Bob']}")
else:
	print("Bob is not a student in this class")
classAttendanceValues = sum(studentAttendance.values()) / len(studentAttendance)
print(f" The avg attendance is {classAttendanceValues}")
print("Destructuring segment")
t = 1, 2
x, y = t
print(x, y)
print(list(studentAttendance.items()))
for student, attendance in studentAttendance.items():
	print(f"{student} : {attendance}")
for t in studentAttendance.items():
	print(t)
peopleAndProfessions = [("Tom", 47, "Contractor"), ("Jim", 30, "Chef"), ("Chris", 25, "Salesman"), ("A", 15, "Model")]
for name, _, profession in peopleAndProfessions:
	print(f"Name: {name}, Profession: {profession}")
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(*tail)
