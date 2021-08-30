"""This program requires the user to input numbers and it checks those numbers through a variety of comparison operators."""
__author__ = "730481483"
left: str = input("Left-hand side ")
right: str = input("Right-hand side ")

left_int: int
left_int = int(left)
right_int: int
right_int = int(right)

print(left + " < " + right + " is " + str(left_int < right_int))

print(left + " >= " + right + " is " + str(left_int >= right_int))

print(left + " == " + right + " is " + str(left_int == right_int))

print(left + " != " + right + " is " + str(left_int != right_int))