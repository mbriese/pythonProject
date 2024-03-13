# this is a comment
# easy variables examples
var1 = 1
var2 = var1
print(var1 + var2)

# easy string examples
st1 = "hello"
st2 = st1 + " world"
print(st2)

# f strings
boyName = "Rolf"
age = 30
namedMessage = f"hello, {boyName.upper()} You are {age} years old!"
print(namedMessage)

# string templates
girlName = "Gretchen"
greeting = "hello, {}"
with_girlName = greeting.format(girlName)
print(with_girlName)

# multiple variables in a string
anotherName = "Bob"
dayToday = "Monday"
multiVariableString = "hello, {}. Today is {}".format(anotherName, dayToday)
print(multiVariableString)

# input functions
nameInput = input("Enter your name: ")
print(nameInput + ' thank you for coming')

# input strings and do math operations
houseSizeInput = input("how many sq feet in your house: ")
sq_ft = int(houseSizeInput)  # now we have an integer
sqMeters = sq_ft / 10.8
resultString = "your house has {} sq meters".format(sqMeters)
print(resultString)
# also can use an f string
print(f"{sq_ft} sq ft is equal to {sqMeters: 2f} sq meters")

# this demos simple concepts to refresh memory on Python
