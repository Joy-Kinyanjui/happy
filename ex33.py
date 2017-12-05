"""
i = 0
numbers = []

while i <6:
    print "At th top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now:" , numbers

    print "At the bottom i is %d" % i

print "numbers:"

for num in numbers:
    print num
"""
"""
books = {'cat':'Notebooks','Dog':'Textbooks','Tiger':'Exercise books'}
pens = ['Bic','Pelican', 'KTTC']

def my_count(object1,object2):
    for obj in object1:
        print "This is book: %r\n" % object1[obj]
    for obj in object2:
        print "This is pen :%r\n" % obj

my_count (books,pens)
print "pens %s" % pens[0]
print "This is book no:%s" % books['Tiger']
"""


"""
def my_loop(number):
    i = 0
    numbers = []

    while i < number:
        print "At th top i is %d" %  i
        numbers.append(i)

        i = i + 1
        print "Numbers now:" , numbers

        print "At the bottom i is %d" %  i

    print "numbers:"

    for num in numbers:
        print num

def square(number):
    return number*number
print "This is my value %r" %  square(5)

"""

Flight_bookings = {'First class':300000,'Second class':250000,'Third class':100000}
Nationality = ['Kenyan', 'German', 'Chinese', 'Mexican']

def plane (Factor1,Factor2):
    for Factor in Factor1:
        print "This is the payment for %s" % Factor1

plane(Flight_bookings,Nationality)
