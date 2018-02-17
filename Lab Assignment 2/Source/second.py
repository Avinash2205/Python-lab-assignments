#Assigning the contact list for the name, number and email
contact_list = [{"name":'Avinash', "number":9490983537, "email":"avinashbanala95@gmail.com"},{"name":"teja", "number":9677060218,
                "email":"surya.2612@gmail.com"},{"name":"legend","number":8166992422,"email":"legendbalayya@gmail.com"}]

# After assigning the input, now asking the user to enter the details
n = input("Enter name to get contact of the list: ")

# Iteration is done in the for loop
for i in contact_list:
# entering the name as prescribed in the dictionary set
    if n in i.values():
# printing the name
        print(i)

# giving the option to the user to enter the contact to get the details
numb = int(input("Enter number from the list to get the contact : "))
# Iterating over contact_list
for j in contact_list:
# conditional statement which is used to check the number in the dictionary
    if numb in j.values():
# Printing if its true
        print(j)

# User should enter the contact and number to edit
ne = input("Enter the name to get the contact and number to edit: ")
# Iterating over the contact_list
for k in contact_list:
# If is used whether to show up it is in dictionary or not
    if ne in k.values():
# Prnting the contact
        print(k)
# Asking user if he want to edit the number
        newnumber = int(input("Edit the number of your own choice to change: "))
# Editing the nimber for the particular user
        k["number"] = newnumber
# Printing the contact
        print(k)