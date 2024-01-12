''' 
Question 1. Write a program to Extract Weather Data from Google in Python. 

'''
import requests
from bs4 import BeautifulSoup

city = "landon"

city = input("Enter City Name : - ")

url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text  # get the temperature
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text   #  get the Time, Sky Description
data = str.split('\n')
time = data[0]
sky = data[1]

print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)



