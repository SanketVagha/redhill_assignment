'''

Question 2. Write Python program to check the validity of a Password.

Primary conditions for password validation:

Minimum 8 characters.
The alphabet must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ]. 

''' 



while True:
    isValid = 0
    password = input("Enter Password :- ")
    upperCase = 0
    lowerCase = 0
    digit = 0
    special = 0
    if len(password) < 8:
        print("Minimum 8 characters.")
    else:
        for i in password:
            if i.isupper():
                upperCase += 1
            elif i.islower():
                lowerCase += 1
            elif i.isdigit():
                digit += 1
            elif i == '_' or i == '@' or i == '$':
                special += 1
            else:
                print("Invalid Character")
                isValid = 1
                break
        if isValid == 0:
            if upperCase > 0 and lowerCase > 0 and digit > 0 and special > 0:
                print("Candidate Password is Strong")
                break
            else:
                if lowerCase == 0:
                    print("The alphabet must be between [a-z]")
                if upperCase == 0:
                    print("At least one alphabet should be of Upper Case [A-Z]")
                if digit == 0:
                    print("At least 1 number or digit between [0-9]")
                if special == 0:
                    print("At least 1 character from [ _ or @ or $ ]")

