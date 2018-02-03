#Python program for finding the triplets
# The below statement is the predefined function in which the variables are assigned
def func(a, n):
    found = False
# defining for loops which is used for the finding of the triplets
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (a[i] + a[j] + a[k] == 0):
                    print(a[i], a[j], a[k])

                    found = True

    if (found == False):
        print(" No Triplets ")


a = [int(x) for x in input().split()]

print(a)

n = len(a)

func(a, n)