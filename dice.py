# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:12:06 2022

@author: Nevermore
"""
# This is the first file

import random
import numpy as np

def roll_d2():
    """ Rolls a two sided die (coin toss).
    
    """
    d2 = random.randint(1,2)
    if d2 >= 1:
        print(f"{d2}")
        return d2

def roll_d3():
    """ Rolls a three sided die.
    
    """
    d3 = random.randint(1,3)
    if d3 >=1:
        print(f"{d3}")
        return d3

def roll_d4():
    """ Rolls a four sided die.

    """
    d4 = random.randint(1,4)
    if d4 >=1:
        print(f"{d4}")
        return d4

def roll_d6():
    """ Rolls a six sided die.
    
    """
    d6 = random.randint(1,6)
    if d6 >=1:
        print(f"{d6}")
        return d6

def roll_d8():
    """ Rolls an eight sided die.
    
    """
    d8 = random.randint(1,8)
    if d8 >=1:
        print(f"{d8}")
        return d8

def roll_d10():
    """ Rolls a ten sided die.
    
    """
    d10 = random.randint(1,10)
    if d10 >=1:
        print(f"{d10}")
        return d10
    
def roll_d12():
    """ Rolls a twelve sided die.
    
    """
    d12 = random.randint(1,12)
    if d12 >=1:
        print(f"{d12}")
        return d12
    
def roll_d20():
    """ Rolls a 20 sided die.
    
    """
    d20 = random.randint(1,20)
    if d20 == 1:
        print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
        return 1
    elif d20 >=2 and d20 <=19:
        print(f"{d20}")
        return d20
    else:
        print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
        return 20

def roll_d100():
    """ Rolls a percentile die.
    
    """
    d100 = random.random()*100
    print(np.round(d100,0))

def main():
    if __name__ == '__main__':
        print("Take a chance, roll the dice!")
        
main()
