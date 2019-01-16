
def get_number():
	number = float(input("enter a float number \n"))
	# print("number entered by you: ")
	return number


while True:
	try:
		print("number entered by you: ", get_number())
	except ValueError:
		print("plesae enter a float number")
	finally: # always gets executed no matter what i.e. after try or after exception, even after an exception which is not defined
		print("execution ended")