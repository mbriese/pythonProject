# list comprehension - quick operations on lists
# operation to create list from another list where we double the elements
numbers = [1, 3, 5]
doubled = []

# put numbers * 2 in doubled
for num in numbers:
    doubled.append(num * 2)
#  print(doubled)

# use List Comprehension to consume numbers into doubled list
doubles = [num * 2 for num in numbers]
#  print(doubles)

# more list comprehension to find names starting with S
friendsList = ["Rolf", "Bob", "Sam", "Stephen", "Susan"]
starts_S = []

for friends in friendsList:
    if friends.startswith("S"):
        starts_S.append(friends)
print(friendsList)
print(starts_S)
starts_WithS = [myfriend for myfriend in friendsList if myfriend.startswith("S")]
print(starts_WithS)
