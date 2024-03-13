# boolean variables for loops
# comparisons: ==, !=, >, <. >, >=, <=
# other comparisons "is" checks whether 2 elements are equal
import random

# remember input is case sensitive .lower() auto converts to lower case for contingency
dayOfWeek = input("What day of the week is it today? ").lower()
if dayOfWeek == "monday":
    print("Have a great start to your week!")
elif dayOfWeek == "friday":
    print("TGIF")
else:
    print("have a great day!")
print("This always prints")

# list of friends
friends = ["Jen", "Rolf", "Bob"]
print("Jen" in friends)  # evaluates to true
# set of movies watched - movies are unique entries / better as a set although no order specified
movies = {"the matrix", "rocky", "green mile"}
user_movie = input("What movie have you watched recently?  ").lower()
if user_movie in movies:
    print(f"I have watched the movie {user_movie} too")
else:
    print("I have not watched that one yet")
print("end of IF statement")

# do you want to play a game while loop and then guess a magic number
playGame = input("Would you want to play a game (Y/n): ").lower()
randomNumber = random.randint(1, 9)
numberOfTries = 1
print(f"for test purposes {randomNumber}")
while playGame in ('y', 'Yes', 'yes') and (numberOfTries < 4):
    userGuess = int(input("Guess a random number between 1 and 9: "))
    if userGuess == randomNumber:
        print(f"You win - you matched my random number {userGuess}")
        break
    elif abs(userGuess - randomNumber) in (1, -1):
        print(f"you were off by one in {numberOfTries} tries")
        break
    else:
        print(f"Not that one {userGuess} + number of tries {numberOfTries}")
        if numberOfTries >= 3:
            print(f"that was the {numberOfTries}  try")
            print("You are out of tries")
            break
    numberOfTries += 1
    playGame = input("Do you want to continue playing? (Y/n): ").lower()
print("Thank you for playing!")

# play with for loops
friends = ["Ann", "Betty", "Cindy Lou", "Donna"]
for friend in friends:
   print(f"{friend} is my friend")
for friend in range(4):
    print(f"{friend} is my friend")

# compute average of grades
grades = [35, 55, 75, 95, 100]
total = 0
gradeTotal = sum(grades)
amount: int = len(grades)
for grade in grades:
    total += grade
average = float(total / amount)
print(f"your average is {average}")
