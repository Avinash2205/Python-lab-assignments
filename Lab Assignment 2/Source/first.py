# The details of the book which are available in the library
det = {
    "Python":40,
    "Data Analytics":50,
    "Jython":30,
    "Big data":20
}


# for loop for assigning of the key value pairs
for k,v in det.items():
# printing the key value pairs
   print(k,v)

# asking the user to enter the minimum and maximum range for the books
a=int(input("Enter the minimum value of the range to get the book: "))
b=int(input("Enter the maximum value of the range to get the book: "))

# checking the values whether the user is able to enter the details within the range
x=dict((k, v)
       for k, v in det.items() if v >=a and v <= b)

# printing the available books
print("You can buy:",x.keys())