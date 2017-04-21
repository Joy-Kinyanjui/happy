
name = 'Joy Kinyanjui'
age = 16 #not a lie
height = 60 # inches
weight = 60 #kilograms
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
height_cm = height * 2.54
weight_grams = weight * 1000

print "Let's talk about %r." % name
print "He's %r centimeters tall." % height_cm
print "He's %r grams heavy." % weight_grams
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." %teeth

#this line is tricky, try o grrt it exactly right
print "If I add %r, %r, and %r I get %r." % (
     age, height_cm, weight_grams,age + height_cm + weight_grams)
