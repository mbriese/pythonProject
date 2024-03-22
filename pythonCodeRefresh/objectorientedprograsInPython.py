# calculate the average of a students grades
# student = {"name": "Bob", "grades": (89, 90, 93, 78, 90)}
#  def average(sequence):
#  return sum(sequence)/len(sequence)
#  print(average(student["grades"]))
#   we use classes in OOP
# methods inside classes
class Student:
	def __init__(self, name, grades):
		# self.name = "Rolf"
		self.name = name
		self.grades = grades
		
	def average(self):
		return sum(self.grades)/len(self.grades)
	
#	def __str__(self):
#		return f"Student {self.name} with grade {self.grades}"
	
	def __repr__(self):
		return f'<Person ("{self.name}", "{self.grades}">'
		
student1 = Student("Rolf", (100, 99))

print(student1.name)
print(student1.grades)
print(Student.average(student1))
print(student1.average())
# we can change properties of an object
student2 = Student("Bob", (92, 91, 90))
print(student2.name)
print(student2.grades)

# magic methods in Python: __init__, __str__, and __repr__
print(student1)
print(student2)
