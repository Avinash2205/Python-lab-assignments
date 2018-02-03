#python code for the list of students attending the class
#  The list containing the number of students who are enrolled in python class
list11 = ['surya', 'sai', 'sagar', 'sandeep']
# The list containing the number of students who are enrolled in web development class
list12 = ['krishna', 'teja', 'babu', 'surya', 'sai', 'sagar', 'sandeep']

# The below print statement is used for printing the students who are common in both the classes
print("Students who are enrolled in both python and web developement classes are: \n")
for a in list11:
    if a in list12:
        print(a)
print('\n')

# The below print statement is used for the students who are enrolled in either of the classes
print("Students who have enrolled in either of web development or python are: \n")

# Checking out the odd one's out from the first available list
for b in list11:
    if b not in list12:
        print(b)

# Checking out the odd one's out from the second available list
for c in list12:
    if c not in list11:
        print(c)