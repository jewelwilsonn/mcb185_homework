
# 10demo.py by JW

import math

print('hello, again') # greeting

# Math, numbers
print(1.5e-2) #example

#Math functions
print( 1 + 1)
print(2**3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))

#numbers aren't real
print(0.1 * 1)
print(0.1 * 3)

#assignment
a = 3 # side of triangle
b = 4 # side of triangle
c = math.sqrt(a**2 + b**2)
print(c)

#type
print(type(a), type(b), type(c), sep=', ', end='!\n') # this ending or, print(sep=' ', end='\n')

#functions
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

#Practice
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h)/2
d = 23
f = d * 1.8 + 32 # celsuis to fahrenheit
print(f)

#Strings
s = 'hello world'
print(s, type(s))

#Conditionals
a = 2
b = 2
if a == b:
	print('a equals b')
	print(a, b)

def is_even(x):
	if x % 2 == 0: return True
	return False
print(is_even(2))
print(is_even(3))

#Boolean
c = 2 == b
print(c)
print(type(c))

#if-elif-else
if a < b:
	print('a<b')
elif a > b:
	print('a>b')
else:
	print('a == b')

#Chaining
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

#Floating Point Warning
a = 0.3
b = 0.2 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else:	print('a == b')
print(abs(a - b)) # 5.51115123125783e-17
if abs(a - b) < 1e-9: print(' close enough')
if math.isclose(a, b): print('close enough')

#String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print ('A < B')
if s2 < s3: print('B < a')

# None Type
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))

#Style

#class 1/28/25
def tm(a, c, g, t):
	length = a + c + g + t
	if length <= 13:
		temp = (a +t) * 2 + (g +c) * 4
		return temp
	else:
		temp = 64.9 + 41 * (g + c - 16.4) / length
		return temp

#(A+T)*2 + (G+C)*4
print('oligo1: ', tm(5, 3, 0, 2))
print('oligo2: ', tm(5, 3, 4, 2))

# other hw
print(ord('A'))
print(ord('B'))
print(ord('Z'))
print(ord('a'))

print(chr(55))
print(chr(56))
print(chr(57))
print(chr(60))
print(chr(61))
print(chr(62))


def letter_to_prob(c):
    return 0.001

def prob_to_symbol(p):
    pass

c = 'A'
pqv = ord(c) - 33
print(10**(-pqv/10))

# nucleotided
def comp(nt):
        if nt == 'A': return 'T'
        if nt == 'C': return 'G'
        if nt == 'G': return 'C'
        if nt == 'T': return 'A'

# max 3


# other hw
 
