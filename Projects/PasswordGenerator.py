#!/usr/bin/env python3

"""
Generate A Random Password With 4 Uppercase Letters, 4 Lowercase Letters, 4 Numbers, And 4 Symbols.
"""

# Import The Required Modules
import random

# A Function To Shuffle All The Characters Of A String
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Uppercase Letters    
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))

# Lowercase Letters
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
lowercaseLetter3=chr(random.randint(97,122))
lowercaseLetter4=chr(random.randint(97,122))

# Numbers
number1=chr(random.randint(48,57))
number2=chr(random.randint(48,57))
number3=chr(random.randint(48,57))
number4=chr(random.randint(48,57))

# Symbols
#symbol1=chr(random.randint(33,152))
symbol1=chr(int(33))
symbol2=chr(int(35))
symbol3=chr(int(36))
symbol4=chr(int(64))

# Generate Password Using All Characters, In A Random Order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + number1 + number2 + number3 + number4 + symbol1 + symbol2 + symbol3 + symbol4
password = shuffle(password)

# Print Password Output
print(password)
