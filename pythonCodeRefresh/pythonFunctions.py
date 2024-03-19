# pyton functions have def functionName(): actionStatements
def hello():
    print("Hello world!")


def user_age():
    age = int(input("Please enter your age in years "))
    age_seconds = age * 365 * 24 * 60 * 60
    print(f"your age in seconds is {age_seconds}")


def add(x, y):
    return x + y


def addThem(dict):
    sums = 0
    for arg in dict.values():
        sums = sums + arg
    return sums


def greetingName(name):
    print(f"Greetings {name}")


def multipleParamsGreeting(name, surname):
    print(f"Greetings Professor {name} {surname}")


def divide(dividend, divisor):
    if divisor != 0:
        result = int(dividend / divisor)
        print(f"the result of {dividend} / {divisor} is {result}")
    else:
        print(f"You can not divide {dividend} by 0 you fool")


# functions with arguments

def addTwo(x, y):
    return x + y


def addList(*lst):
    total = 0
    for num in range(0, len(lst)):
        total = total + lst[num]
    print(f"sum of elements in list is {total}")
    return total


def divide_result(dividend, divisor):
    if divisor != 0:
        result = int(dividend / divisor)
        return result
    else:
        return "You fool"


def multiplyMultipleArgs(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total


def apply(*args, operator):
    print(f"Operator is {operator} and *args list {args}")
    if operator == "*":
        return multiplyMultipleArgs(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operators provided to apply()."


hello()
user_age()
addTwo(1, 1)
greetingName("Bob")
multipleParamsGreeting("Bob", "Smith")
multipleParamsGreeting(surname="Smith", name="Bob")
divide(dividend=3, divisor=1)
divide(9, 3)
divide(3, 0)

add(5, 8)
sumfromAddEmUp = addTwo(5, 8)
print(f"the sum from add them up is {sumfromAddEmUp}")
print("using returnAddEnds result below")
print(addTwo(5, 8))
print(divide_result(15, 3))
print(divide_result(15, 0))

# multiple arguments sent to functions
print("functions with unknown number of arguments")
print(f"multiply variable number of arguments sent as params (1 ,3, 5) to multiply is {multiplyMultipleArgs(1, 3, 5)}")

# destructuring lists into functions
numsList = [3, 5]
sumOfList = addList(*numsList)
print(f"destructure list into an add function {numsList} is {sumOfList}")

# destructure dictionary into function using **
numsDictionary = {"a": 15, "b": 25}

print(f"using a dictionary {numsDictionary} for params in sum function) ")

# problems with dictionary - try later anotherDictionary = {"a": 15, "b": 25, "c": 1}
anotherList = [15, 25, 1]
# print("Sum: ", apply(*anotherDictionary, operator="+"))
print("Sum: ", apply(15, 25, 1, operator="+"))
print("Multiply: ", apply(15, 25, 1, operator="*"))
