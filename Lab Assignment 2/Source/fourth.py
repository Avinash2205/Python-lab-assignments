# import statement for the numpy
# Numpy is useful for mainly N-dimensional array objects
import numpy as np
# giving the random declaration for the values to be occurred in the list
a = np.random.randint(0, 20, 15)
# printing the random list
print("The list which is to be appeared random are:")
print(a)
# Printing the frequent value in the list
print("Most frequent value in the List is :")
print(np.bincount(a).argmax())