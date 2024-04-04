def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend/divisor


grades = []
students = [
    {'name': 'John', 'grades': [75, 90]},
    {'name': 'Rolf', 'grades': [83.5]},
    {'name': 'Jane', 'grades': [100, 90]}
]

print("Welcome to the average grade program.")
try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} averaged {average: 2f}')
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades.")
else:
    print("--- completed calculating the averages ---")
finally:
    print("--- End of student grades calculation ---")
