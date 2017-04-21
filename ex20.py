from sys import argv # System module

script, input_file = argv # unpacking the module

def print_all(f):# The function has an arguments that happens to be a file
    print f.read() # Command to read the file

def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file) # opening the file
print "First let's print the whole file:\n"

print_all(current_file)

print"Now let's rewind, kind of like a tape."

rewind(current_file)

print"Let's print three lines:"

current_file = 1
print_a_line(current_line, current_file) # current_line is the linecount

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
