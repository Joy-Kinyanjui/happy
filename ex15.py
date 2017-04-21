from sys import argv # Module

script, filename = argv # Unpacking the argumentative variable from the system module

txt = open(filename) # The open function\method

print "Here's your file %r:" % filename
print txt.read() # the read function\method

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open (file_again)

print txt_again.read()
