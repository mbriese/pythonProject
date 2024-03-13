# lambda functions
# starting from previous function defn and going forward
# regular function
def add(x: object, y: object) -> object:
    return sum(x, y)


# lambda function - not usually given a name or used like this
addemup = lambda x, y: x + y

print(add(5, 7))
print(addemup(5, 7))
# more commonly used like this
print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2


print(double(2))
sequence = [1, 3, 5, 7, 9]
print(sequence)
doubled = [double(x) for x in sequence]
print(doubled)
# note you need to turn map into a list to print it out
anotherdoubled = list(map(lambda x: x * 2, sequence))
print(anotherdoubled)
