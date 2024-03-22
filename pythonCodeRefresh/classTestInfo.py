class ClassTest:
	def instance_Method(self):
		print(f"Called instance_method of {self}")
	
	@classmethod
	def class_method(cls):
		print(f"Called class method of {cls}")
		
	
	@staticmethod
	def static_method():
		print("called static method")
		
## Instance method - called by creating an object of class
# test = ClassTest()
# test.instance_Method()
# ClassTest.instance_Method(test)

## working with class methods - it creates an instance of class by calling the method
ClassTest.class_method()

## working with static method - doesn't take an argument
ClassTest.static_method()



	