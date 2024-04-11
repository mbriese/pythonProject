from operator import itemgetter


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(f"Result: {result}")


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"{expected} Not found")


friends = [
    {"name": "Rolf Smith", "age": 20},
    {"name": "Adam Wood", "age": 30},
    {"name": "Anne Pun", "age": 40}
]


def get_friends_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", itemgetter("name")))

try:
    print(search(friends, "Rolf Smith", get_friends_name))
    print(search(friends, "Anne Pun", lambda friend: friend["name"]))
    print(search(friends, "Jane Austin", get_friends_name))
except RuntimeError as e:
    print(e)
