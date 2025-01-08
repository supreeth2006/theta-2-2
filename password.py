def validation_password(password):
    if len(password) >= 8:
        if any(char.isdigit() for char in password):
            if any(char.isalpha() for char in password):
                if any(char in "!@#$%^&*()" for char in password):
                    print("Password is valid")
                else:
                    print("Password is incorrect .It must contain atleast one special char.")
            else:
                print("password is incorrect .It must contain atleast one letter")
        else:
            print("password is incorrect .It must contain atleast one digit")
    else:
        print("password is incorrect .It must contain atleast eight char")

password = input("Enter your Password")
res=validation_password(password)
print(res)