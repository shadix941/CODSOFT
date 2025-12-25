import random
import string
#function to generate password
def generate_password( min_length,numbers=True,special_characters=True):
    letter= string.ascii_letters
    digits= string.digits
    special= string.punctuation

    characters=letter
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special

    pwd=""
    meets_criteria= False
    has_number= False
    has_special=False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True

        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if special_characters:
            meets_criteria=meets_criteria and has_special

    return pwd
while True: #check the user input if it is numbers or not 
    user_input = input("Enter the minimum length: ")
    try:
        min_length = int(user_input)
        if min_length > 0:
            break
        else:
            print("Length must be greater than 0.")
    except ValueError:
        print("Please enter numbers only.")

has_number = input("Do you want numbers (y/n)? ").lower() == "y"
has_special = input("Do you want special characters (y/n)? ").lower() == "y"
 #generate the password
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)

