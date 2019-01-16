
class Person(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		print('Accessing person')
		# super(Person, self).__init__()
		# self.arg = arg

	def get_details(self):
		return self.name


class Student(Person):
	"""docstring for ClassName"""
	def __init__(self, name, branch, year):
		self.name = name
		self.branch = branch
		self.year = year
		super().__init__(self.name)

	def get_details(self):
		print("%s studies in %s dep and was enrolled in %s" %(self.name, self.branch, self.year))

class Teacher(Person):
	"""docstring for ClassName"""
	def __init__(self, name, paper):
		self.name = name
		self.paper = paper
		super().__init__(self.name)
		# self.arg = arg

	def get_details(self):
		print("%s teaches %s" %(self.name, self.paper))


person1 = Person('ABC')
student = Student('ABC', 'CS', '2016')
teacher = Teacher("DEF", ['Python', 'Linear Algebra'])

print(person1.get_details())
student.get_details()
teacher.get_details()

print(Student.__mro__)
print(Teacher.__mro__)
		
		
		