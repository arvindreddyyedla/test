# A valid email address has four parts:
# Validation information was studied from https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-

# Recipient name
# @ symbol
# Domain name
# Top-level domain

# Email validation and domain extraction program
 
#re module give us support to in python to test or check  regular expresions
import re

regularExpEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,}\b'
# explain above any character before .  and @ followed by . and ensuring only one @ in the whole string
# function returning whether the given string is valid email or not
def returnEmailValidation(emailAddress):
    # checking whether email is valid from method from the re module
    # and verify the match
    valid = re.fullmatch(regularExpEmail, emailAddress)
    if (re.fullmatch(regularExpEmail, emailAddress)):
        return 1
    else:
        return 0
 
#infinte loop intilization
while True:
    # Input from user to get the email
    email = input("\nPlease enter email to validate : ")
    try:
        # Checking for the empty string case and verify the same
        if len(email) == 0:
            print("Please enter a string to validate. Provided empty string")
            continue

        # email validation from the method
        isEmailValid = returnEmailValidation(email) == 1
        if isEmailValid:
            splitEmail = email.split('@')
            # extracting domain on verifying email in success case
            print("\n"+email+" is valid email.\nYour domain name is "+splitEmail[1])

        else:
            print("\n"+email+" is not a valid email")

    except: 
         print("\n"+email+" is not a valid email")

    #expecting user input to verify the break the infinite loop.
    userChoice = input("\nPress enter to provide more email ids or type 999 to exit: ")
    if userChoice == "999":
        break

print("\n")