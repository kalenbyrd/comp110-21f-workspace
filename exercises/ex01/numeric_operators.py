""""""
left: str = input("Left-hand side ")
right: str = input("Right-hand side ")

left_int: int
left_int = int(left)
right_int: int
right_int = int(right)

print(left + " ** " + right + " is " + str(left_int ** right_int))

print(left + " / " + right + " is " + str(left_int / right_int))

print(left + " // " + right + " is " + str(left_int // right_int))

print(left + " % " + right + " is " + str(left_int % right_int))