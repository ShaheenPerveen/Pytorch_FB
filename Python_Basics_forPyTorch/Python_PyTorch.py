#!/usr/bin/python

class Student(object):

    def __init__(self, name, branch, dr):
        self.name = name
        self.branch = branch
        self.dr = dr

    def print_details(self):
        print("Name: ", self.name)
        print("Branch: ", self.branch)
        print("DR: ", self.dr)
        print("above are the details")

std1 = Student('SP', 'BT', '10')
std1.print_details()

class Rectangle():

	def __init__(self, length, breadth, unit_cost, fencing_cost):
		self.length = length
		self.breadth = breadth
		self.unit_cost = unit_cost
		self.fencing_cost = fencing_cost

	def get_perimeter(self):
		return 2 * (self.length + self.breadth)

	def get_area(self):
		return self.length * self.breadth

	def get_flooring_cost(self):
		area = self.get_area()
		return area * self.unit_cost

	def get_fencing_cost(self):
		fence = self.get_perimeter()
		return fence * self.fencing_cost


land =  Rectangle(120, 100, 10, 20)

land.get_flooring_cost()
land.get_fencing_cost()

print("area of land is %d and it will cost %d for flooring" % (land.get_area(), land.get_flooring_cost()))
print("perimeter of land is %d and it will cost %d for fencing" % (land.get_perimeter(), land.get_fencing_cost()))