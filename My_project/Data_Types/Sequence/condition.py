def is_valid_password (password):
    if len(password) <8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "@$#%*()~?/<>_=--+" for char in password):
        return False
    return 'Strong password'
print(is_valid_password(input("Please enter password")))
#another example
#define a variable for the email
email = input("enter your email:")
#define condition for valid email
if "@" in email:
    if "." in email:
            if email.index("@") > 0:
                if email.count("@") == 1:
                    print("valid email")