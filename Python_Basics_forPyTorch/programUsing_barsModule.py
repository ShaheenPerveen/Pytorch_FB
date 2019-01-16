"""
program to use calculation_SP module in different ways
"""
# import calculation_SP

import sys
sys.path.append('/home/fractaluser/ShaheenPerveenF01930_Backup/Pytorch_FB/Lesson2/')

import calculation_SP_1

x = int(input("please enter the first number \n"))
y = int(input("please enter the second number \n"))

def print_operations(x,y):
	print('printing output using calculation_SP_1 module')
	print(calculation_SP_1.add(x,y))
	print(calculation_SP_1.subtract(x,y))
	print(calculation_SP_1.product(x,y))
	print(calculation_SP_1.division(x,y))

def main():
	print(print_operations(x,y))

if __name__ == '__main__':
	main()


