def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)

    return a / b

def addition(a, b):
    print "ADDITION %d + %d" % (a, b)
    return a + b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
books = addition(25,64)

print "Age: %d, Height: %d, Weight: %d, IQ: %d, Books: %d," % (age, height, weight, iq, books)

 # A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"

print  age+(age-height * weight /iq)



# Study Drills

def multiply (a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def add (a,b):
    print "ADDITION %d + %d" % (a, b)
    return a + b

def sqr (a):
    print "SQUARE %d " % (a)
    return a**2

def divide (x, y):
    print "DIVISION %d / %d" % (x,y)
    return x / y

shoes =float(raw_input("Number of shoes"))
hats = float(raw_input("Number of  hats"))
sweaters =float(raw_input("Number of sweaters"))
houses = float(raw_input("Number of houses available"))
people =float(raw_input("Number of people"))

"""
 Solving equation
 y = a(x**2+x/y)

 """

wearables = multiply(shoes,add(sqr(hats),divide(houses,people)))
print ("I have this many", wearables, "just for me")
