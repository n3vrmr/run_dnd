# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:55:10 2022

@author: Nevermore
"""
# This is the second file

char_level = int(input("Character level: "))
def proficiency_mod():
    """ Defines your proficiency modifier according to your character level.
    
    """
    if char_level <=4:
        return 2
    elif char_level >=5 and char_level <=8:
        return 3
    elif char_level >=9 and char_level <=12:
        return 4
    elif char_level >=13 and char_level <=16:
        return 5
    elif char_level >=17 and char_level <=20:
        return 6

print(f"Proficiency modifier: {proficiency_mod()}")
