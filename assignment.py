''' 
Question 1. Write a program to Extract Weather Data from Google in Python. 

'''

import requests
from bs4 import BeautifulSoup

city = "banglore"

city = input("Enter City Name")

url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split('\n')
time = data[0]
sky = data[1]
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
pos = strd.find('Wind')
other_data = strd[pos:]
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)



'''

Question 2. Write Python program to check the validity of a Password.

Primary conditions for password validation:

Minimum 8 characters.
The alphabet must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ]. 

''' 

password = input("Enter Password")

upperCase = 0
lowerCase = 0
digit = 0
special = 0
isValid = 1
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
            isValid = 0
            break
    if isValid == 1:
        if upperCase > 0 and lowerCase > 0 and digit > 0 and special > 0:
            print("Candidate Password is Strong")
        else:
            if lowerCase == 0:
                print("The alphabet must be between [a-z]")
            if upperCase == 0:
                print("At least one alphabet should be of Upper Case [A-Z]")
            if digit == 0:
                print("At least 1 number or digit between [0-9]")
            if special == 0:
                print("At least 1 character from [ _ or @ or $ ]")

'''
Question 3. What are the main differences between C and C++?


C Language is POP (Program Oriented Language) Oriented Language Means It's Not Refer To The Class and Object.

C++ Language is OOP(Object Oriented Language) Oriented Language Means It's Refer To The Class and Object.


'''


'''
Question 4.4. What do you know about Timers in Arduino?


Timers is Modules in Arduino To Provides timing functionalities.

It's Provide Like Provide Delay Between Two Events, Periodic Event Handling  

'''

'''
Question 5. What are some commonly used libraries in Arduino?


Arduino Libraries Most Commonly used in working with Hardware and Manipulation Data,

'''