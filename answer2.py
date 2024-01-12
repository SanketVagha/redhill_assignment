'''

Question 2. Write Python program to check the validity of a Password.

Primary conditions for password validation:

Minimum 8 characters.
The alphabet must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ]. 

''' 

#  Strong Password Not Found till loop executed

while True:
    isValid = 0
    password = input("Enter Password :- ")
    upperCase = 0
    lowerCase = 0
    digit = 0
    special = 0
    if len(password) < 8:  # check the length of the password
        print("Minimum 8 characters.")
    else:
        for i in password: # string divided into single charactor
            if i.isupper():  # upper latter check
                upperCase += 1
            elif i.islower(): # lower latter check
                lowerCase += 1
            elif i.isdigit():  # digit check 
                digit += 1
            elif i == '_' or i == '@' or i == '$':  # given special charactor _ @ $ check 
                special += 1
            else:                   # any other charactor find out in password break the loop and send the error message
                print("Invalid Character")
                isValid = 1
                break
        if isValid == 0:
            if upperCase > 0 and lowerCase > 0 and digit > 0 and special > 0:   # all the primary condition satisfya check
                print("Candidate Password is Strong")
                break
            else:
                if lowerCase == 0:      # lower latter not available in password check
                    print("The alphabet must be between [a-z]")
                if upperCase == 0:      #  upper latter not available in password check
                    print("At least one alphabet should be of Upper Case [A-Z]")
                if digit == 0:          # digit not available in password check
                    print("At least 1 number or digit between [0-9]")
                if special == 0:        # special charactor available in password check
                    print("At least 1 character from [ _ or @ or $ ]")

