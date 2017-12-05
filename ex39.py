"""
#Create a mapping of the state to abbreviation

states = {
    'Oregon':'OR',
    'Florida':'FL',
    'Carlifornia':'CA',
    'Newyork':'NY',
    'Michigan':'MI'
}






#Create a basic set of states and some cities in them

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities

cities['NY'] = 'Colarado village'
cities['OR'] = 'Portland'

# Print out some cities

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#Print out some states
print'-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ",states['Florida']

 #Do it using the state then cities dict
print '_' * 10
print "Michigan has: " , cities[states['Michigan']]
print "florida has:" , cities[states['Florida']]

#print every state in abbreviation

print '-' * 10
for state, abbrev in states.items():
    print "%s has the abbreviated as%s" % (state, abbrev)

#print every city in state
print "-" * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now do both at the same time
"""



"""
School = {'Subjects':{'Comp':'Kinanga','Math':'Njoroge','English':'Karanja'},'Teachers':'Kibe'}

Clubs = School['Subjects']
General = School['Teachers']

print "This is a subject:%s"  % Clubs['Comp']
print "This is the teacher on duty this week:%s" % General
"""


#This is are the towns in the counties  in our lovely country Kenya

Counties = {'Kajiado':'Ngong','Kirinyaga':'Kerugoya','Nairobi':'Langata'}

#Printing the towns in the Counties

Towns = Counties['Kirinyaga']
print "-" * 15
print "This is the town I live in %s" % Towns
