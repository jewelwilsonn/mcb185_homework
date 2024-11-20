import math

a = 3 # side of triangle
b = 4 # side of triangle
c = math.sqrt(a**2 + b**2) # hypotenuse
print(c)

print(type(a), type(b), type(c))

print(type(a), type(b), type(c), sep=', ')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

x = pythagoras(3, 4)
print(x)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))
print(pythagoras(1, 1))
