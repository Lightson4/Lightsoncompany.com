
#inputing module
import math
result = int(input("plese enter your number:"))
square = math.sqrt(result)
print(square)
#importing specific functions of veriables
from math import sqrt
result2 = int(input("plese enter your number:"))
square2 = sqrt(result2)
print(square2)
#importing all functions in a module (wildcart)
from math import *
result3 = int(input("plese enter your angle:"))
square3 = cos(result3)
print(square3)
#renaming a function or module
import math as light
result4 = int(input("plese enter your number:"))
square4 = light.sqrt(result4)
print(square4)
from math import sqrt as nelson
result5 = int(input("plese enter your number:"))
square5 = nelson(result5)
print(square5)

'''#importig costom module
import my_modu
print(my_modu.greet('Ben'))
print(my_modu.addition(5,4))
#python standard libray module eg os, sys, datetime, ramdon
import os 
print(os.getcwd())
import random
print(random.randint(1, 9))
#installing and importing third party
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
# creating spellchecker
from spellchecker import SpellChecker
corrector = SpellChecker()
word = input("enter a word:")
if word in corrector:
    print("correct")
else:
    correct_word = corrector.correction(word)
    print(f"correct spelling is", {correct_word})
    '''