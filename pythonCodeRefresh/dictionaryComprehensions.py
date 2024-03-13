users = [
    (0, "Bob", "password"),
    (1, "Cam", "C1234"),
    (2, "Dan", "D2345"),
    (3, "Earl", "E3456"),
    (4, "Fred", "F4567"), ]

# get element[1] in mapping == name
username_maps = {user[1]: user for user in users}
print(username_maps)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
# check to see if the username and password details are correct, dont check ID element
_, username, password = username_maps[username_input]
if password_input == password:
   print("Your details are correct")
else:
    print("Your details are incorrect.")