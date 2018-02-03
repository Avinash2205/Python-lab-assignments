#Python program for the password validation
Spsymbols =['$','@','#','!']
while True:
    password = input("Type password :")
    if len(password)< 6:
        print("Password Should consists of atleast 6-16 characters long ")
        continue
    elif len(password)> 16 :
        print("Password should have maximum of  16 characters ")
        continue
    elif not any(char.isdigit() for char in password):
        print('the password should have at least one number from the number list')
        continue
    elif not any(char.isupper() for char in password):
        print('It should consists of atleast one uppercase letter')
        continue
    elif not any(char.islower() for char in password):
        print('It should consists of  atleast one lowercase letter')
        continue
    elif not any(char in Spsymbols for char in password):
        print('It must consists atleast one of this special symbols : $@#!')
        continue
    else:
        print("The password validated was correct")
        print(password)
        break