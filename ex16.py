from sys import argv # system module

script, filename = argv # unpacking the module

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # gathering info from the person directly

print "Opening the file..."
target = open(filename,'w') # opening the file

print "Truncting the file. Goodbye!"
target . truncate() # Empting the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

myline = (line1+line2+line3)
target.write(myline)

print "And finally, we close it."
target.close() # closing the file

txt = open (filename)
print "Open the name of the file "

print txt.read
